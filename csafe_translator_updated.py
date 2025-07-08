import logging
logging.basicConfig(
    format='%(asctime)s | %(levelname)s: [%(funcName)s] %(message)s',
    level=logging.DEBUG,
    # level=logging.INFO,
    )

from .csafe_constants import *
from .csafe_command_reference import *
# from ..enum_maps.pm5_enumerations import get_enum_string


"""
C-SAFE Protocol ::
    The CSAFE protocol was created to facilitate communication between fitness equipment 
    and a host computer. The “public” CSAFE protocol implementation provides a basic 
    framework for configuring workouts, and monitoring progress of those workouts, through 
    a “state machine” style mechanism. So in order to be compatible with existing fitness 
    equipment controllers, a public CSAFE implementation has been included with the PM. 
"""


# UNIQUE CSAFE FRAME FLAGS
"""
The “byte-stuffing” algorithm simply substitutes two bytes for 
each of the unique bytes listed below.
"""
EXTENDED_FRAME_START_FLAG = 0xF0    # 240 
STANDARD_FRAME_START_FLAG = 0xF1    # 241
DESTINATION_ADDRESS_FLAG = 0xFD     # 253 - Used for PM5
SOURCE_ADDRESS_FLAG = 0x00          # 0 - Used for PM5
STOP_FRAME_FLAG = 0xF2              # 242
BYTE_STUFFING_FLAG = 0xF3           # 243 - Essentially an escape character

class CSAFEMessageHandler(object):
    """
    The CSAFEMessageHandler class is responsible for converting between CSAFE command 
    and readable reponse formats. It does this by going throught the following steps:

    1. Py3rg calls the pm_message_sender method with a command.
    2. pm_message_sender calls the to_csafe method to convert the command to a CSAFE message format.
    3. The CSAFE message is sent to the the Performance Monitor.
    4. The Performance Monitor sends a response back to the host.
    5. The pm_message_sender method calls the from_csafe method to convert the CSAFE response to a readable format.
    6. The readable response is returned to the caller.
    """
    # Dictionaries for CSAFE commands
    # Formatted as {cmd_name: namedtuple("Command", ["id", "args", "wrapper"])}
    commands = {**SHORT_COMMANDS, **LONG_COMMANDS, **PM5_COMMANDS}
    
    # Response dictionaries for CSAFE responses
    # Formatted as {resp_id: namedtuple(resp_id, cmd_name, field_byte_schema))}
    responses = {**SHORT_RESPONSES, **LONG_RESPONSES, **PM5_RESPONSES}
    

    def __init__(self):
        return

    def _get_response_spec(self, cmd_id, wrapper=None):
        """
        Get the response specification for a given command ID and optional wrapper.
        Returns: Response Spec Object for Shema reference
        """
        key = (wrapper << 8  | cmd_id) if wrapper else cmd_id
        logging.debug(f"Getting response spec for key: {key}")
        resp = self.responses.get(key)
        if resp:
            logging.debug(f"Found response spec: {resp}")
            return resp
        else:
            logging.warning(f"No response spec found for key: {key}")
            return None
    
    @staticmethod
    def _validate_frame_length(frame: bytes) -> bytes:
        """
        For CSAFE protocol compatibility, the following frame length restrictions are invoked for the PM physical link:
            1. A maximum frame size of 120 bytes including start/stop flags, checksum and byte stuffing
            2. All flow control handled natively as part of physical link
        HID Reports 
            ID #1 - 20 bytes + 1 byte report ID
            ID #2 - 120 bytes + 1 byte report ID
            ID #4 - 62 bytes + 1 byte report ID or
            ID #4 - 500 bytes + 1 byte report ID 
        """
        frame_len = len(frame)

        if frame_len <= 20:
            report_id = 0x01
            payload_frame_len = 20
        elif frame_len <= 62:
            report_id = 0x04
            payload_frame_len = 62
        elif frame_len <= 120:
            report_id = 0x02
            payload_frame_len = 120
        # max CSAFE frame size is supposed to be 500 bytes but HID reports allow for 500 bytes
        # elif frame_len <= 500:
        #     report_id = 0x04
        #     padded_len = 500
        else:
            raise ValueError("Frame length exceeds maximum HID frame size of 120 bytes.")

        padding = [0x00] * (payload_frame_len - frame_len)
        hid_payload = [report_id] + frame + padding
        logging.debug(f"Final HID payload length: {len(hid_payload)}")

        return (hid_payload, report_id)

    def _to_csafe(self, host_arguments: list, extended_frame: bool = False) -> bytes:
        """
        Converts a list of command names into a valid CSAFE command frame.
        Returns a byte list ready to send to the device.
        """
        # Build the CSAFE message body
        message_body = []
        for cmd_name in host_arguments:
            if cmd_name not in self.commands:
                raise ValueError(f"Unknown command: {cmd_name}")
            cmd = self.commands[cmd_name]

            if cmd.wrapper is not None:
                message_body.append(cmd.wrapper)

            if cmd.id < 0x80:
                # Long command
                message_body.append(cmd.id)
                arg_bytes = cmd.args or []
                message_body.append(len(arg_bytes))
                message_body.extend(arg_bytes)
            else:
                # Short command
                message_body.append(cmd.id)

        logging.debug(f"Message body before wrapping: {message_body}")

        # Frame construction
        if extended_frame:
            frame = [
                EXTENDED_FRAME_START_FLAG,
                DESTINATION_ADDRESS_FLAG,
                SOURCE_ADDRESS_FLAG,
                len(message_body),
            ] + message_body
        else:
            frame = [STANDARD_FRAME_START_FLAG] + message_body

        # Checksum (XOR of relevant frame fields)
        checksum = (frame[3] if extended_frame else 0)
        for b in message_body:
            checksum ^= b

        frame += [checksum, STOP_FRAME_FLAG]
        logging.debug(f"Frame before stuffing: {frame}")

        # Byte stuffing for extended frames only
        if extended_frame:
            stuffed = []
            escape_map = {
                0xF0: [0xF3, 0x00],
                0xF1: [0xF3, 0x01],
                0xF2: [0xF3, 0x02],
                0xF3: [0xF3, 0x03],
            }
            for byte in frame:
                if byte in escape_map:
                    stuffed.extend(escape_map[byte])
                    logging.debug(f"Byte stuffing: {hex(byte)} → {escape_map[byte]}")
                else:
                    stuffed.append(byte)
            final_frame = stuffed
            logging.debug(f"Final byte CSAFE frame [{len(stuffed)} bytes]: {stuffed}")
        else:
            final_frame = frame

        # Final payload with report ID and HID padding
        payload, report_id = self._validate_frame_length(frame=final_frame)
        logging.debug(f"Final payload frame [{len(payload)} bytes]: {payload}")

        return (payload, report_id)




    def _parse_response(self, cmd_id, wrapper, data):
        return #...

    def _from_csafe(self, pm_response):

        return #...

    def pm_message_sender(self, device, command, pretty=False):
        """
        Sends a CSAFE command to the device.
        In practice, this would send via USB/HID.
        For now this is a stub.
        """
        logging.debug(f"Preparing to send command: {command}")
        csafe = self._to_csafe(host_arguments=command)
        csafe_packet = csafe[0]
        report_id = csafe[1]
        logging.debug(f"Encoded command to CSAFE: {csafe_packet}")
        
        # --------------------------------------------------------------------#
        # SEND THE COMMAND TO THE DEVICE
        # Write the command
        try:
            bytes_written = device.write(csafe_packet)
            if bytes_written == 0:
                logging.error("No response from device from HID write.")
                return None
            logging.debug(f"Response byte length: {bytes_written}")
        
        except IOError as e:
            logging.error(f"Error sending command to device: {e}")
            return None

        # Read the device response
        response = []
        try:
            transmission = device.read(bytes_written,timeout_ms=2000)
            if not transmission or len(transmission) < 3:
                logging.error("No or incomplete transmission received.")
                return None

            report_id = transmission[0]
            resp_payload = transmission[1:]
            logging.debug(f"Report ID: {report_id}, Payload: {resp_payload}")
            # Next: Unstuff, parse frame, validate checksum
        except IOError as e:
            logging.error(f"Error reading response: {e}")
            return None

        # TODO : Parse transmission


        return None




def _from_csafe(self, pm_response: list):
    if pm_response[0] != STANDARD_FRAME_START_FLAG or pm_response[-1] != STOP_FRAME_FLAG:
        raise ValueError("Invalid CSAFE frame format")

    body = pm_response[1:-2]
    received_checksum = pm_response[-2]

    checksum = 0
    for b in body:
        checksum ^= b
    if checksum != received_checksum:
        raise ValueError("Checksum mismatch")

    return self._parse_response(body)


def _parse_response(self, response_body: list):
    # Load all known responses
    all_responses = {}
    all_responses.update(SHORT_RESPONSES)
    all_responses.update(LONG_RESPONSES)
    all_responses.update(PM5_RESPONSES)

    parsed = []
    i = 0
    while i < len(response_body):
        cmd_id = response_body[i]
        i += 1

        if cmd_id not in all_responses:
            parsed.append((cmd_id, None))
            continue

        response = all_responses[cmd_id]
        field_spec = response.fields
        field_data = []

        # Handle numeric field length spec like [1], [4,1], etc.
        for field in field_spec:
            if isinstance(field, int):
                if i + field > len(response_body):
                    raise ValueError("Incomplete response field data")
                field_data.append(response_body[i:i + field])
                i += field
            elif isinstance(field, str):
                # Placeholder for named schema, like 'uint16[]'
                field_data.append(f"Unhandled field schema: {field}")
            else:
                raise TypeError("Unexpected field type in response spec")

        parsed.append((cmd_id, field_data))

    return parsed

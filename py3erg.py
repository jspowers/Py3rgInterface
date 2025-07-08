import time

import hid as cyhid
from csafe.csafe_translator import CSAFEMessageHandler

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s | %(levelname)s: %(message)s',
    level=logging.DEBUG,
    # level=logging.INFO,
    )

MIN_FRAME_GAP = .050 #in seconds

devices = dict()
for d in cyhid.enumerate():
    manufact_name = d['manufacturer_string']
    device_id = d['product_id']
    device_name = d['product_string']
    
    devices[manufact_name] = devices.get(manufact_name, dict())
    if device_id not in devices[manufact_name]:
        devices[manufact_name][device_id] = device_name
    
# -------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------- #
# PyRowHID Class Object 

class PyRowHID(object):
    VENDOR_ID = 6052
    DEVICE_ID = 90

    def __init__(self):
        # logging.info(f"Attempting to open device vendor: {self.VENDOR_ID}, id: {self.DEVICE_ID}")
        # self.dev = hid.Device(self.VENDOR_ID, self.DEVICE_ID)
        # self.manufacturer = self.dev.manufacturer
        # self.product = self.dev.product
        # self.serial_no = self.dev.serial
        
        self.dev = cyhid.device()
        logging.info(f"Attempting to open device vendor: {self.VENDOR_ID}, id: {self.DEVICE_ID}")
        self.dev.open(self.VENDOR_ID, self.DEVICE_ID)
        self.manufacturer = self.dev.get_manufacturer_string()
        self.product = self.dev.get_product_string()
        self.serial_no = self.dev.get_serial_number_string()

        logging.info(f"Device Found - {self.product} : {self.serial_no}")

        self.__lastsend = int(time.time())
    

    def close(self):
        logging.info("closing connection to device")
        self.dev.close()

    def flush_device(self, timeout_ms=20, max_reads=10):
        """Flush lingering reports from the PM input buffer."""
        flushed = 0
        for _ in range(max_reads):
            try:
                data = self.dev.read(64, timeout_ms)
                if data:
                    flushed += 1
                    logging.debug(f"[flush_device] Flushed: {data}")
                else:
                    break  # No more data
            except Exception as e:
                logging.warning(f"[flush_device] Error reading device: {e}")
                break
        if flushed == 0:
            logging.debug("[flush_device] No leftover data to flush")

    def get_machine_version(self, enum_convert=False):
        command = ['CSAFE_GETVERSION_CMD']
        handler = CSAFEMessageHandler()
        response = handler.pm_message_sender(device=self.dev, command=command)
        logging.debug(f"CSAFEMessageHandler response: {response}")
        return response



    def get_machine_status(self, enum_convert=False):
        """
        Returns the status of the erg
        """
        command = ['CSAFE_GETSTATUS_CMD']
        handler = CSAFEMessageHandler()
        response = handler.pm_message_sender(device=self.dev, command=command)
        logging.debug(f"CSAFEMessageHandler response: {response}")
        
        return response
    

    def get_workout(self, enum_convert=False):
        """
        Returns overall workout data
        """

        command = [
            'CSAFE_PM_GET_WORKOUTTYPE', 
            # 'CSAFE_PM_GET_WORKOUTSTATE',
            # 'CSAFE_PM_GET_INTERVALTYPE', 
            # 'CSAFE_PM_GET_WORKOUTINTERVALCOUNT'
        ]
        handler = CSAFEMessageHandler()
        response = handler.pm_message_sender(device=self.dev, command=command)

        return response
    




if __name__ == '__main__':
    print(devices)
    try:
        test = PyRowHID()
    except Exception as e:
        logging.error(f"Error opening device: {e}")
        exit(1)
    logging.debug("Getting Device Status ... ")
    print('---------------------------------------')

    # transmission = test.dev.read(121, timeout_ms=1000)
    # while transmission != 0:
    #     time.sleep(.1)
    #     transmission = test.dev.read(121, timeout_ms=1000)
    #     logging.debug(f"Transmission after 1 wait: {transmission}")


    # test.get_machine_version()
    test.get_machine_status()
    # test.get_workout()
    test.close()
    
# csafe_commands.py
from collections import namedtuple

# -------------------------------------------------------------------------------------------- #
# HID REPORT IDS
report_ids = {
    # report_id : max_packet_len 
    0x01: 20,
    0x02: 120,
    0x04: 62
} 

# -------------------------------------------------------------------------------------------- #
# CSAFE COMMANDS FORMATE

"""
CSAFE Command Format:

Description     Size (Bytes)    Value
Long Command    1               0x00 - 0x7F (range(0, 127))
Short Command   1               0x80 - 0xFF (range(128, 255))
Data Byte Count 1               0 - 255 
Data            Variable        0 - 255

Multiple complete commands can be included in a single frame, but no partial commands or responses are allowed. When sending a frame consisting of multiple commands to a secondary device, the resulting response frame consists of multiple command responses. 
"""

Command = namedtuple("Command", ["id", "args", "wrapper"])

SHORT_COMMANDS = {
    'CSAFE_GETSTATUS_CMD': Command(0x80,[],None),
    'CSAFE_RESET_CMD': Command(0x81,[],None),
    'CSAFE_GOIDLE_CMD': Command(0x82,[],None),
    'CSAFE_GETVERSION_CMD': Command(0x91, [], None)
}

LONG_COMMANDS = {
    'CSAFE_PM_GET_FORCEPLOTDATA': Command(0x6B, [1], 0x1A),
}

PM5_COMMANDS = {
    
    'CSAFE_PM_GET_WORKOUTTYPE': Command(0x89, [], 0x1A),
    'CSAFE_PM_GET_WORKOUTSTATE': Command(0x8D, [], 0x1A),
    'CSAFE_PM_GET_INTERVALTYPE': Command(0x8E, [], 0x1A),
    'CSAFE_PM_GET_WORKOUTINTERVALCOUNT': Command(0x9F, [], 0x1A),
    'CSAFE_PM_GET_WORKTIME': Command(0xA0, [], 0x1A),
    'CSAFE_PM_GET_WORKDISTANCE': Command(0xA3, [], 0x1A),
    'CSAFE_PM_GET_ERRORVALUE': Command(0xC9 , [], 0x1A),
    'CSAFE_PM_GET_RESTTIME': Command(0xCF, [], 0x1A),
}

# -------------------------------------------------------------------------------------------- #
# CSAFE RESPONSES FORMATS 
"""
CSAFE Response Format:

Description             Size (Bytes)    Value
Status                  1               0x00 – 0x7F
Command Response Data   Variable        0 - 255
Command                 1               0x00 – 0xFF
Data Byte Count         1               1 - 255
Data                    Variable        0 - 255

- byte_count: The first byte tells you how many bytes of data follow. You’ll use this to determine the size of the array.
- 'uint16[]': After that, interpret the remaining bytes as a list of 2-byte little-endian unsigned integers.
"""

Response = namedtuple("Response", ["id", "name", "fields"])

SHORT_RESPONSES = {
    0x80: Response(0x80,'CSAFE_GETSTATUS_CMD',[0]),
    0x81: Response(0x81,'CSAFE_RESET_CMD',[0]),
    0x82: Response(0x82,'CSAFE_GOIDLE_CMD',[0]),
    0x91: Response(0x91, 'CSAFE_GETVERSION_CMD', [7])
}

LONG_RESPONSES = {
    0x6B: Response(0x6B, 'CSAFE_PM_GET_FORCEPLOTDATA', fields=['byte_count', 'uint16[]']), 
}
    
PM5_RESPONSES = {
    0x89: Response(0x89, 'CSAFE_PM_GET_WORKOUTTYPE', [1]), 
    0x8D: Response(0x8D, 'CSAFE_PM_GET_WORKOUTSTATE', [1]), 
    0x8E: Response(0x8E, 'CSAFE_PM_GET_INTERVALTYPE', [1]), 
    0x9F: Response(0x9F, 'CSAFE_PM_GET_WORKOUTINTERVALCOUNT', [1]), 
    0xA0: Response(0xA0, 'CSAFE_PM_GET_WORKTIME', [4, 1]), 
    0xA3: Response(0xA3, 'CSAFE_PM_GET_WORKDISTANCE', [4, 1]), 
    0xC9: Response(0xC9, 'CSAFE_PM_GET_ERRORVALUE', [2]), 
    0xCF: Response(0xCF, 'CSAFE_PM_GET_RESTTIME', [2]), 
    }



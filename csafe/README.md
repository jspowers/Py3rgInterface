# CSAGE Translator Documentation 

## Concept2 PM5 CSAFE References
[Performance Monitor CSAFE Communication Definition](https://www.concept2.co.uk/files/pdf/us/monitors/PM5_CSAFECommunicationDefinition.pdf)
The above like was used to generate the translation logic between this program and the CSAFE commands that are used to interface with with Performance Monitor device.

## What is C-SAFE
**1. What is C-SAFE**
C-SAFE stands for Communication Standard for Fitness Equipment. It's a command-response protocol made up of little "messages" that get packed into binary frames. You send a command, the monitor responds with data — stroke rate, watts, distance, etc.
**2. How It’s Structured (High Level)**
Each message frame includes:
- A start flag to say, “Hey, this is the beginning.”
- A length byte (how many bytes are coming next)
- A sequence of commands (CSAFE codes)
- A checksum
- A stop flag to say, “We’re done here.”


## C-SAFE Command Tuple Structure
Each command has an associate
    - id : 
    - args : (if applicable) Expected Input Parameters. Used if some CSAFE commands require additional data when sent. This might mean the command expects 1 byte of argument data.
        ```python
        # Hypothetical command
        'CSAFE_SETPOWER_CMD': Command(0x93, [1], None)
        ```
    - wrapper : (if applicable) Special Handling for PM5-Specific Extensions 

## The ``
The CSAFEMessageHandler class is the responsible middle layer for translating commands to C-SAFE compatible bytess
- `_to_csafe`: Converts high-level command tuples into CSAFE-compliant byte lists.
- `_from_csafe`: Parses CSAFE response byte lists into human-readable values using your get_enum_string.
- `pm_message_sender`: Wraps the full process (currently using a mock response).



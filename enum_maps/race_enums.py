from enum import Enum
import logging

# -------------------------------------------------------------------------------------------------- #
# --- RACE ENUMERATIONS --- #
"""
RACE ENUMERATIONS
    - StartType
    - RaceOperationType
    - RaceState
    - RaceType
    - RaceStartState
    - StatusType
    - DisplayUpdateRate
"""

# Start Type
class StartType(Enum):
    """
    Enum for the start types.
    """
    RANDOM = 0    # /**< Random type (0). */
    COUNTDOWN = 1  # /**< Countdown type (1). */
    RANDOMMODIFIED = 2  # /**< Random modified type (2). */
    IMMEDIATE = 3  # /**< Immediate type (3). */
    WAITFORFLYWHEEL = 4  # /**< Wait for flywheel type (4). */

# Race Operation Type
class RaceOperationType(Enum):
    """
    Enum for Race operation types.
    """
    DISABLE = 0    # /**< Disable type (0). */
    PARTICIPATIONREQUEST = 1  # /**< Participation request type (1). */
    SLEEP = 2    # /**< Sleep type (2). */
    ERGINIT = 3  # /**< Erg initialization type (3). */
    PHYADDRINIT = 4  # /**< Physical address/lane initialization 
    RACEWARMUP = 5  # /**< Race warmup type (5). */
    RACEINIT = 6    # /**< Race initialization type (6). */
    TIMESYNC = 7    # /**< Time synchronization type (7). */
    RACEWAITTOSTART = 8     # /**< Race wait to start type (8). */
    START = 9   # /**< Race start type (9). */
    FALSESTART = 10     # /**< Race false start type (10). */
    TERMINATE = 11  # /**< Race terminate type (11). */
    IDLE = 12   # /**< Race idle type (12). */
    TACHSIMENABLE = 13  # /**< Tach simulator enable type (13). */
    TACHSIMDISABLE = 14     # /**< Tach simulator disable type (14). */

# Race State
class RaceState(Enum):
    """
    Enum for Race State.
    """
    IDLE = 0  # , /**< Race idle state (0). */
    COUNTDOWN = 1     # , /**< Race countdown state (1). */
    ROWING = 2    # , /**< Race rowing state (2). */
    INTERVAL_REST = 3     # , /**< Race interval rest state (3). */
    END_INTERVAL = 4  # , /**< Race end interval state (4). */
    END_WORKOUT_RACE = 5  # , /**< Race end workout state (5). */
    TERMINATE_WORKOUT_RACE = 6    # , /**< Race terminate workout state (6). */
    FALSESTART = 7    # , /**< Race false start state (7). */
    INACTIVE = 8  # , /**< Race inactive state (8). */

# Race Type
class RaceType(Enum):
    """
    Enum for Race Type.
    """
    FIXEDDIST_SINGLEERG = 0     #  /**< Fixed distance, individual type (0). */
    FIXEDTIME_SINGLEERG = 1     #  /**< Fixed time, individual type (1). */
    FIXEDDIST_TEAMERG = 2       #  /**< Fixed distance, team type (2). */
    FIXEDTIME_TEAMERG = 3       #  /**< Fixed time, team type (3). */
    WORKOUTRACESTART = 4        #  /**< Workout race start type (4). */
    FIXEDCAL_SINGLEERG = 5      #  /**< Fixed calorie, individual type (5). */
    FIXEDCAL_TEAMERG = 6        #  /**< Fixed calorie, team type (6). */
    FIXEDDIST_RELAY_SINGLEERG = 7       #  /**< Fixed distance, relay individual type (7). */
    FIXEDTIME_RELAY_SINGLEERG = 8       #  /**< Fixed time, relay individual type (8). */
    FIXEDCAL_RELAY_SINGLEERG = 9        #  /**< Fixed calorie, relay individual type (9). */
    FIXEDDIST_RELAY_TEAMERG = 10        #  /**< Fixed distance, relay team type (10). */
    FIXEDTIME_RELAY_TEAMERG = 11        #  /**< Fixed time, relay team type (11). */
    FIXEDCAL_RELAY_TEAMERG = 12     #  /**< Fixed calorie, relay team type (12). */
    FIXEDDIST_MULTIACTIVITY_SEQUENTIAL_SINGLEERG = 13       #  /**< Fixed distance, multiactivity individual type, sequential use (13). */
    FIXEDTIME_MULTIACTIVITY_SEQUENTIAL_SINGLEERG = 14       #  /**< Fixed time, multiactivity individual type, sequential use (14). */
    FIXEDCAL_MULTIACTIVITY_SEQUENTIAL_SINGLEERG = 15        #  /**< Fixed calorie, multiactivity individual type, sequential use (15). */
    FIXEDDIST_MULTIACTIVITY_SEQUENTIAL_TEAMERG = 16     #  /**< Fixed distance, multiactivity team type, sequential use (16). */
    FIXEDTIME_MULTIACTIVITY_SEQUENTIAL_TEAMERG = 17     #  /**< Fixed time, multiactivity team type, sequential use (17). */
    FIXEDCAL_MULTIACTIVITY_SEQUENTIAL_TEAMERG = 18      #  /**< Fixed calorie, multiactivity team type, sequential use (18). */
    FIXEDDIST_ERGATHLON = 19        #  /**< Fixed distance, Ergathlon type (19). */
    FIXEDTIME_ERGATHLON = 20        #  /**< Fixed time, Ergathlon type (20). */
    FIXEDCAL_ERGATHLON = 21     #  /**< Fixed calorie, Ergathlon type (21). */
    FIXEDDIST_MULTIACTIVITY_SIMULTANEOUS_SINGLEERG = 22     #  /**< Fixed distance, multiactivity individual type, simultaneous use (22). */
    FIXEDTIME_MULTIACTIVITY_SIMULTANEOUS_SINGLEERG = 23     #  /**< Fixed time, multiactivity individual type, simultaneous use (23). */
    FIXEDCAL_MULTIACTIVITY_SIMULTANEOUS_SINGLEERG = 24      #  /**< Fixed calorie, multiactivity individual type, simultaneous use (24). */
    FIXEDDIST_MULTIACTIVITY_SIMULTANEOUS_TEAMERG = 25       #  /**< Fixed distance, multiactivity team type, simultaneous use (25). */
    FIXEDTIME_MULTIACTIVITY_SIMULTANEOUS_TEAMERG = 26       #  /**< Fixed time, multiactivity team type, simultaneous use (26). */
    FIXEDCAL_MULTIACTIVITY_SIMULTANEOUS_TEAMERG = 27        # /**< Fixed calorie, multiactivity team type, simultaneous use (27). */
    FIXEDDIST_BIATHLON = 28     #  /**< Fixed distance, Biathlon type (28). */
    FIXEDCAL_BIATHLON = 29      #  /**< Fixed calorie, Biathlon type (29). */
    FIXEDDIST_RELAY_NOCHANGE_SINGLEERG = 30     #  /**< Fixed distance, no change prompt, relay individual type (30). */
    FIXEDTIME_RELAY_NOCHANGE_SINGLEERG = 31     #  /**< Fixed time, no change prompt, relay individual type (31). */
    FIXEDCAL_RELAY_NOCHANGE_SINGLEERG = 32      #  /**< Fixed calorie, no change prompt, relay individual type (32). */
    FIXEDTIME_CALSCORE_SINGLEERG = 33       #  /**< Fixed time, calorie score, individual type (33). */
    FIXEDTIME_CALSCORE_TEAMERG = 34     # /**< Fixed time, calorie score, team type (34). */
    FIXEDDIST_TIMECAP_SINGLEERG = 35        #  /**< Fixed time, calorie score, individual type (35). */
    FIXEDCAL_TIMECAP_SINGLEERG = 36     # /**< Fixed time, calorie score, team type (36). */}

# Race Start State
class RaceStartState(Enum):
    """
    Enum for Race Start State.
    """
    INIT = 0        #, /**< Init state (0). */
    PREPARE = 1     #, /**< Prepare state (1). */
    WAITREADY = 2       #, /**< Wait ready state (2). */
    WAITATTENTION = 3       #, /**< Wait attention state (3). */
    WAITROW = 4     #, /**< Wait row state (4). */
    COUNTDOWN = 5       #, /**< Countdown state (5). */
    ROW = 6     #, /**< Row state (6). */
    FALSESTART = 7      # /**< False start state (7). */

# Status Type
class StatusType(Enum):
    NONE = 0        # /**< None (0). */
    BATTERY_LEVEL1_WARNING = 1      # /**< Battery level 1 warning, status value = (current battery level/max battery value) * 100 (1). */
    BATTERY_LEVEL2_WARNING = 2      # /**< Battery level 2 warning, status value = (current battery level/max battery value) * 100 (2). */
    LOGDEVICE_STATE = 3     # /**< Log device state, status value = log device status (3). */
    POWERSOURCE_STATE = 4       # /**< Power source, status value = power source status (4). */
    LOGCARD_WORKOUTLOGGED_STATUS = 5        # /**< Log device workout logged, status value = workout logged status (5). */
    FLYWHEEL_STATE = 6      # /**< Flywheel, status value = not turning, turning (6). */
    BAD_UTILITY_STATE = 7       # /**< Bad utility, status value = correct utilty, wrong utility (7). */
    FWUPDATE_STATUS = 8     # /**< Firmware update, status value = no update pending, update pending, update complete (8). */
    UNSUPPORTEDUSBHOSTDEVICE = 9        # /**< Unsupported USB host device, status value = unused (9). */
    USBDRIVE_STATE = 10     # /**< USB host drive, status value = uninitialized, initialized (10). */
    LOADCONTROL_STATUS = 11     # /**< Load control, status value = all loads allowed, usb host not allowed, backlight not allowed, neither allowed (11). */
    USBLOGBOOK_STATUS = 12      # /**< USB log book, status value = directory missing/corrupt, file missing/corrupt, validated (12). */
    LOGSTORAGECAPACTYWARNING_STATUS = 13        # /**< Log storage capacity warning, status value = current used capacity (13). */
    FACTORYCALIBRATION_WARNING = 14     # /**< Full calibration warning, status value = unused (14). */
    VERIFYCALIBRATION_WARNING = 15      # /**< Verify calibration warning, status value = unused (15). */
    SERVICECALIBRATION_WARNING = 16     # /**< Service calibration warning, status value = unused (16). */


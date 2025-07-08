from enum import Enum
import logging

"""
MACHINE ENUMERATIONS
    - MachineType
    - MachineState
    - ErgModelType
    - SreenType
    - ScreenValueWorkoutType
    - ScreenValueRaceType
    - ScreenValueCSAFEType
    - ScreenStatus
"""

# Erg Machine Type
class MachineType(Enum):
    """
    Enum for the machine types.
    """
    STATIC_D = 0    #, /**< Model D, static type (0). */
    STATIC_C = 1    #, /**< Model C, static type (1). */
    STATIC_A = 2    #, /**< Model A, static type (2). */
    STATIC_B = 3    #, /**< Model B, static type (3). */
    STATIC_E = 5    #, /**< Model E, static type (5). */
    STATIC_SIMULATOR = 7    #, /**< Rower simulator type (7). */
    STATIC_DYNAMIC = 8    #, /**< Dynamic, static type (8). */
    SLIDES_A = 16    #, /**< Model A, slides type (16). */
    SLIDES_B = 17    #, /**< Model B, slides type (17). */
    SLIDES_C = 18    #, /**< Model C, slides type (18). */
    SLIDES_D = 19    #, /**< Model D, slides type (19). */
    SLIDES_E = 20    #, /**< Model E, slides type (20). */
    LINKED_DYNAMIC = 32    #, /**< Dynamic, linked type (32). */
    STATIC_DYNO = 64    #, /**< Dynomometer, static type (32). */
    STATIC_SKI = 128    #, /**< Ski Erg, static type (128). */
    STATIC_SKI_SIMULATOR = 143    #, /**< Ski simulator type (143). */
    BIKE = 192    #, /**< Bike, no arms type (192). */
    BIKE_ARMS = 193    #, /**< Bike, arms type (193). */
    BIKE_NOARMS = 194    #, /**< Bike, no arms type (194). */
    BIKE_SIMULATOR = 207    #, /**< Bike simulator type (207). */
    MULTIERG_ROW = 224    #, /**< Multi-erg row type (224). */
    MULTIERG_SKI = 225    #, /**< Multi-erg ski type (225). */
    MULTIERG_BIKE = 226    #, /**< Multi-erg bike type (226). */
    NUM = 227    #, /**< Number of machine types (227). */

# Erg Machine State
class MachineState(Enum):
    """
    Enum for the machine states.
    """
    RESET = 0    #, /**< Reset state (0). */
    READY = 1    #, /**< Ready state (1). */
    WORKOUT = 2    #, /**< Workout state (2). */
    WARMUP = 3   #, /**< Warm-up state (3). */
    RACE = 4    #, /**< Race state (4). */
    POWEROFF = 5    #, /**< Power-off state (5). */
    PAUSE = 6    #, /**< Pause state (6). */
    INVOKEBOOTLOADER = 7    #, /**< Invoke boot loader state (7). */
    POWEROFF_SHIP = 8    #, /**< Power-off ship state (8). */
    IDLE_CHARGE = 9    #, /**< Idle charge state (9). */
    IDLE = 10    #, /**< Idle state (10). */
    MFGTEST = 11    #, /**< Manufacturing test state (11). */
    FWUPDATE = 12    #, /**< Firmware update state (12). */
    DRAGFACTOR = 13    #, /**< Drag factor state (13). */
    DFCALIBRATION = 100    #, = 100 /**< Drag factor calibration state (100). */

# Erg Model Type
class ErgModelType(Enum):
    """
    Enum for the erg model types.
    """
    TYPE_D = 0
    TYPE_C = 1
    TYPE_A = 2

# Screen Type
class ScreenType(Enum):
    """
    Enum for Screen Type.
    """
    NONE = None     # /**< None type (None). */
    WORKOUT = 0     # /**< Workout type (0). */
    RACE = 1        # /**< Race type (1). */
    CSAFE = 2       # /**< CSAFE type (2). */
    DIAG = 3        # /**< Diagnostic type (3). */
    MFG = 4         # /**< Manufacturing type (4). */

# Screen Value (Workout Type)
class ScreenValueWorkoutType(Enum):
    """
    Enum for Screen Value Workout Type.
    """
    NONE = 0        # /**< None value (0). */
    PREPARETOROWWORKOUT = 1     # /**< Prepare to workout type (1). */
    TERMINATEWORKOUT = 2        # /**< Terminate workout type (2). */
    REARMWORKOUT = 3        # /**< Rearm workout type (3). */
    REFRESHLOGCARD = 4      # /**< Refresh local copies of logcard structures(4). */
    PREPARETORACESTART = 5      # /**< Prepare to race start (5). */
    GOTOMAINSCREEN = 6      # /**< Goto to main screen (6). */
    LOGCARDBUSYWARNING = 7      # /**< Log device busy warning (7). */
    LOGCARDSELECTUSER = 8       # /**< Log device select user (8). */
    RESETRACEPARAMS = 9     # /**< Reset race parameters (9). */
    CABLETESTSLAVE = 10     # /**< Cable test slave indication(10). */
    FISHGAME = 11       # /**< Fish game (11). */
    DISPLAYPARTICIPANTINFO = 12     # /**< Display participant info (12). */
    DISPLAYPARTICIPANTINFOCONFIRM = 13      # /**< Display participant info w/ confirmation (13). */
    CHANGEDISPLAYTYPETARGET = 20        #  20, /**< Display type set to target (20). */
    CHANGEDISPLAYTYPESTANDARD = 21      # /**< Display type set to standard (21). */
    CHANGEDISPLAYTYPEFORCEVELOCITY = 22     # /**< Display type set to forcevelocity (22). */
    CHANGEDISPLAYTYPEPACEBOAT = 23      # /**< Display type set to Paceboat (23). */
    CHANGEDISPLAYTYPEPERSTROKE = 24     # /**< Display type set to perstroke (24). */
    CHANGEDISPLAYTYPESIMPLE = 25        # /**< Display type set to simple (25). */
    CHANGEUNITSTYPETIMEMETERS = 30      #  30, /**< Units type set to timemeters (30). */
    CHANGEUNITSTYPEPACE = 31        # /**< Units type set to pace (31). */
    CHANGEUNITSTYPEWATTS = 32       # /**< Units type set to watts (32). */
    CHANGEUNITSTYPECALORICBURNRATE = 33     # /**< Units type set to caloric burn rate(33). */
    TARGETGAMEBASIC = 34        # /**< Basic target game (34). */
    TARGETGAMEADVANCED = 35     # /**< Advanced target game (35). */
    DARTGAME = 36       # /**< Dart game (36). */
    GOTOUSBWAITREADY = 37       # /**< USB wait ready (37). */
    TACHCABLETESTDISABLE = 38       # /**< Tach cable test disable (38). */
    TACHSIMDISABLE = 39     # /**< Tach simulator disable (39). */
    TACHSIMENABLERATE1 = 40     # /**< Tach simulator enable, rate = 1:12 (40). */
    TACHSIMENABLERATE2 = 41     # /**< Tach simulator enable, rate = 1:35 (41). */
    TACHSIMENABLERATE3 = 42     # /**< Tach simulator enable, rate = 1:42 (42). */
    TACHSIMENABLERATE4 = 43     # /**< Tach simulator enable, rate = 3:04 (43). */
    TACHSIMENABLERATE5 = 44     # /**< Tach simulator enable, rate = 3:14 (44). */
    TACHCABLETESTENABLE = 45        # /**< Tach cable test enable (45). */
    CHANGEUNITSTYPECALORIES = 46        # /**< Units type set to calories(46). */
    VIRTUALKEY_A = 47       # /**< Virtual key select A (47). */
    VIRTUALKEY_B = 48       # /**< Virtual key select B (48). */
    VIRTUALKEY_C = 49       # /**< Virtual key select C (49). */
    VIRTUALKEY_D = 50       # /**< Virtual key select D (50). */
    VIRTUALKEY_E = 51       # /**< Virtual key select E (51). */
    VIRTUALKEY_UNITS = 52       # /**< Virtual key select Units (52). */
    VIRTUALKEY_DISPLAY = 53     # /**< Virtual key select Display (53). */
    VIRTUALKEY_MENU = 54        # /**< Virtual key select Menu (54). */
    TACHSIMENABLERATERANDOM = 55        # /**< Tach simulator enable, rate = random (55). */
    SCREENREDRAW = 255      # /**< Screen redraw (255). */

# Screen Value (Race Type)
class ScreenValueRaceType(Enum):
    """
    Enum for Screen Value Race Type.
    """
    NONE = 0        # /**< None value (0). */
    SETPHYSICALADDR = 1     # /**< Set physical address (1). */
    CONFIRMPHYSICALADDR = 2     # /**< Confirm physical address (2). */
    WARMUPFORRACE = 3       # /**< Warmup for race (3). */
    PREPARETORACE = 4       # /**< Prepare to race (4). */
    FALSESTARTRACE = 5      # /**< False start race (5). */
    TERMINATERACE = 6       # /**< Terminate race (6). */
    AUTOSETPHYSADDR = 7     # /**< Automatically set physical address (7). */
    SETPARTICIPANTLIST = 8      # /**< Indication that participant list is being set (8). */
    SYNCRACETIME = 9        # /**< Indication that race time sync is occuring (9). */
    PREPARETOSLEEP = 10     # /**< Preparation for sleeping erg (10). */
    RESETRACEPARAMS = 11        # /**< Reset race parameters (11). */
    SETDEFAULTCOMMPARAMS = 12       # /**< Set default communication parameters (12). */
    RACEIDLE = 13       # /**< Enter race idle (13). */
    ERGADDRESSSTATUS = 14       # /**< Display current erg physical address (14). */
    RACEIDLEROW = 15        # /**< Enter race idle row (15). */
    DISPLAYRACEBITMAP = 16      # /**< Display race bitmap (16). */
    DISPLAYRACETEXTSTRING = 17      # /**< Display race text string (17). */
    SETLOGICALADDR = 18     # /**< Set logical address (18). */
    CONFIRMLOGICALADDR = 19     # /**< Confirm logical address (19). */
    ERGSLAVEDISCOVERY = 20      # /**< Discover secondary Ergs (20). */
    GOTOMAINSCREEN = 21     # /**< Goto to main screen (21). */
    RESETERG = 22       # /**< Reset Erg (22). */
    SETUNITSTYPEDEFAULT = 23        # /**< Set units type to default (23). */
    TACHSIMDISABLE = 39     # /**< Tach simulator disable (39). */
    TACHSIMENABLERATE1 = 40     # /**< Tach simulator enable, rate = 1:12 (40). */
    TACHSIMENABLERATE2 = 41     # /**< Tach simulator enable, rate = 1:35 (41). */
    TACHSIMENABLERATE3 = 42     # /**< Tach simulator enable, rate = 1:42 (42). */
    TACHSIMENABLERATE4 = 43     # /**< Tach simulator enable, rate = 3:04 (43). */
    TACHSIMENABLERATE5 = 44     # /**< Tach simulator enable, rate = 3:14 (44). */
    TACHCABLETESTENABLE = 45        # /**< Tach cable test enable (45). */
    ERGATHLONMODEDISABLE = 46       # /**< Ergathlon mode disable (46). */
    RS485FIRMWAREUPDATEPROGRESS = 47        # /**< RS-485 firmware update in progress (47). */
    TERMINATERACEANDPRESERVERESULTS = 48        # /**< Terminate race and preserve results (48). */
    TACHSIMENABLERATERANDOM = 49        # /**< Tach simulator enable, rate = random (49). */
    SCREENREDRAW = 255      #  /**< Screen redraw (255). */

# Screen Value (CSAFE Type)
class ScreenValueCSAFEType(Enum):
    """
    Enum for Screen Value CSAFE Type.
    """
    NONE = 0        # /**< None value (0). */
    USERID = 1      # /**< Enter user ID (1). */
    PREPARETOROWWORKOUT = 2     # /**< Prepare to workout (2). */
    GOTOMAINSCREEN = 3      # /**< Goto to main screen (3). */
    CUSTOM = 4      # /**< Goto custom screen (4). */
    RACECHANOPEN = 250      # /**< Open racing channel (250). */
    RACECHANCLOSE = 251     # /**< Close racing channel (251). */
    SCREENREDRAW = 255      # /**< Screen redraw (255). */

# Screen Status
class ScreenStatus(Enum):
    """
    Enum for Screen Status.
    """
    INACTIVE = 0
    PENDING = 1
    INPROGRESS = 2

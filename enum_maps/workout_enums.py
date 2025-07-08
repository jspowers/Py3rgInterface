from enum import Enum
import logging


# -------------------------------------------------------------------------------------------------- #
#  --- WORKOUT ENUMBERATIONS --- #
"""
WORKOUT ENUMBERATIONS
    - WorkoutType
    - IntervalType
    - WorkoutState
    - RowingState
    - WorkoutDurationType
    - WorkoutNumber
    - WorkoutProgrammingMode
"""

# Erg Workout Type
class WorkoutType(Enum):
    """
    Enum for the workout types.
    """
    JUSTROW_NOSPLITS = 0
    JUSTROW_SPLITS = 1
    FIXEDDIST_NOSPLITS = 2
    FIXEDDIST_SPLITS = 3
    FIXEDTIME_NOSPLITS = 4
    FIXEDTIME_SPLITS = 5
    FIXEDTIME_INTERVAL = 6
    FIXEDDIST_INTERVAL = 7
    VARIABLE_INTERVAL = 8
    VARIABLE_UNDEFINEDREST_INTERVAL = 9
    FIXEDCALORIE_SPLITS = 10
    FIXEDWATTMINUTE_SPLITS = 11
    FIXEDCALS_INTERVAL = 12
    NUM = 13

# Interval Type
class IntervalType(Enum):
    """
    Enum for the interval types.
    """
    TIME = 0   # /**< Time interval type (0). */
    DIST = 1   # /**< Distance interval type (1). */
    REST = 2   # /**< Rest interval type (2). */
    TIMERESTUNDEFINED = 3      # /**< Time undefined rest interval type (3). */
    DISTANCERESTUNDEFINED = 4      # /**< Distance undefined rest interval type (4). */
    RESTUNDEFINED = 5      # /**< Undefined rest interval type (5). */
    CALORIE = 6    # /**< Calorie interval type (6). */
    CALORIERESTUNDEFINED =   7  # /**< Calorie undefined rest interval type (7). */
    WATTMINUTE = 8     # /**< Watt-minute interval type (8). */
    WATTMINUTERESTUNDEFINED = 9    # /**< Watt-minute undefined rest interval type (9). */
    NONE = 255     # /**< No interval type (255 ). */

# Workout State
class WorkoutState(Enum):
    """
    Enum for the workout states.
    """
    WAITTOBEGIN = 0     # /**< Wait to begin state (0). */
    WORKOUTROW = 1  # /**< Workout row state (1). */
    COUNTDOWNPAUSE = 2  # /**< Countdown pause state (2). */
    INTERVALREST = 3    # /**< Interval rest state (3). */
    INTERVALWORKTIME = 4    # /**< Interval work time state (4). */
    INTERVALWORKDISTANCE = 5    # /**< Interval work distance state (5). */
    INTERVALRESTENDTOWORKTIME = 6   # /**< Interval rest end to work time state (6). */
    INTERVALRESTENDTOWORKDISTANCE = 7   # /**< Interval rest end to work distance state (7). */
    INTERVALWORKTIMETOREST = 8  # /**< Interval work time to rest state (8). */
    INTERVALWORKDISTANCETOREST = 9  # /**< Interval work distance to rest state (9). */
    WORKOUTEND = 10     # /**< Workout end state (10). */
    TERMINATE = 11  # /**< Workout terminate state (11). */
    WORKOUTLOGGED = 12  # /**< Workout logged state (12). */
    REARM = 13  # /**< Workout rearm state (13). */

# Rowing State
class RowingState(Enum):
    """
    Enum for the rowing states.
    """
    INACTIVE = 0    # /**< Inactive (0). */
    ACTIVE = 1  # /**< Active (1). */

# Workout Duration Type
class WorkoutDurationType(Enum):
    """
    Enum for the workout duration types.
    """
    TIME = 0
    CALORIES = 0x40
    DISTANCE = 0x80
    WATTMIN = 0xC0

# Workout Number
class WorkoutNumber(Enum):
    PROGRAMMED = 0  #  /**< Programmed (0). */
    DEFAULT_1 = 1   #  /**< Standard list 1 (1). */
    DEFAULT_2 = 2   #  /**< Standard list 2 (2). */
    DEFAULT_3 = 3   #  /**< Standard list 3 (3). */
    DEFAULT_4 = 4   #  /**< Standard list 4 (4). */
    DEFAULT_5 = 5   #  /**< Standard list 5 (5). */
    CUSTOM_1 = 6    #  /**< Custom list 1 (6). */
    CUSTOM_2 = 7    #  /**< Custom list 2 (7). */
    CUSTOM_3 = 8    #  /**< Custom list 3 (8). */
    CUSTOM_4 = 9    #  /**< Custom list 4 (9). */
    CUSTOM_5 = 10   #  /**< Custom list 5 (10). */
    MSD_1 = 11  #  /**< Favorite list 1 (11). */
    MSD_2 = 12  #  /**< Favorite list 2 (12). */
    MSD_3 = 13  #  /**< Favorite list 3 (13). */
    MSD_4 = 14  #  /**< Favorite list 4 (14). */
    MSD_5 = 15  #  /**< Favorite list 5 (15). */
    NUM = 16    # /**< Number of workouts (16). */

# Workout Programming Mode
class WorkoutProgrammingMode(Enum):
    DISABLE = 0
    ENABLE = 1

# Display Update Rate
class DisplayUpdateRate(Enum):
    """
    Enum for Display Update Rate.
    """    
    DISPLAY_UPDATERATE_5HZ = 0  # /**< 5Hz (0). */
    DISPLAY_UPDATERATE_4HZ = 1  # /**< 4Hz (1). */
    DISPLAY_UPDATERATE_2HZ = 2  # /**< 2Hz (2). */

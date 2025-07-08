from enum import Enum
import logging

# -------------------------------------------------------------------------------------------------- #
# --- DISPLAY ENUMERATIONS --- #
"""
DISPLAY ENUMERATIONS
    - DisplayUnitsType
    - DisplayFormatType
"""

# Display Units Type
class DisplayUnitsType(Enum):
    TIMEMETERS = 0  #    /**< Time/meters display units (0). */
    PACE = 1    #    /**< Pace display units (1). */
    WATTS = 2   #    /**< Watts display units (2). */
    CALORICBURNRATE = 3 #    /**< Caloric burn rate display units (3). */
    CALORIES = 4    #   /**< Calorie display units (4). */

# Display Format Type
class DisplayFormatType(Enum):
    """
    Enum for the display format types.
    """
    STANDARD = 0    # /**< Standard display type (0). */
    FORCEVELOCITY = 1   # /**< Force curve display type (1). */
    PACEBOAT = 2    # /**< Pace boats display type (2). */
    PERSTROKE = 3   # /**< Store rate/heart rate display type (3). */
    SIMPLE = 4  # /**< Large format display type (4). */
    TARGET = 5  # /**< Target display type (5). */
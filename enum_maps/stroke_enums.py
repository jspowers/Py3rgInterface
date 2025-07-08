from enum import Enum
import logging

# -------------------------------------------------------------------------------------------------- #
#  --- STROKE ENUMBERATIONS --- #
"""
STROKE ENUMERATIONS
    - StrokeState
    - StrokeRateState
"""

# Stroke State
class StrokeState(Enum):
    """
    Enum for the stroke states.
    """
    WAITING_FOR_WHEEL_TO_REACH_MIN_SPEED_STATE = 0   #  /**< FW to reach min speed state (0). */
    WAITING_FOR_WHEEL_TO_ACCELERATE_STATE = 1    #  /**< FW to accelerate state (1). */
    DRIVING_STATE = 2    #  /**< Driving state (2). */
    DWELLING_AFTER_DRIVE_STATE = 3   #  /**< Dwelling after drive state (3). */
    RECOVERY_STATE = 4   #  /**< Recovery state (4). */

# Stroke Rate State
class StrokeRateState(Enum):
    IDLE = 0    # /**< Idle state (0). */
    STEADY = 1  # /**< Steady state (1). */
    INCREASING = 2  # /**< Increasing state (2). */
    DECREASING = 3  #/**< Decreasing state (3). */
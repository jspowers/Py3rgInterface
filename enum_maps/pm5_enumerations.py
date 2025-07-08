from enum import Enum
import logging
from machine_enums import *
from workout_enums import *
from stroke_enums import *
from display_enums import *
from race_enums import *


"""
Created from mapping file from Concept2:
https://www.concept2.co.uk/files/pdf/us/monitors/PM5_CSAFECommunicationDefinition.pdf
"""
# ---------------------------------------------------------------------------------- #
# --- ENUMERATION MAPS --- #

MACHINE_ENUMS = {
    'machine_type': MachineType,
    'machine_state': MachineState,
    'erg_model_type': ErgModelType,
    'screen_type': ScreenType,
    'screen_value_workout_type': ScreenValueWorkoutType,
    'screen_value_race_type': ScreenValueRaceType,
    'screen_value_csafe_type': ScreenValueCSAFEType,
    'screen_status': ScreenStatus,
}

WORKOUT_ENUMS = {
    'workout_type': WorkoutType,
    'interval_type': IntervalType,
    'workout_state': WorkoutState,
    'rowing_state': RowingState,
    'workout_duration_type': WorkoutDurationType,
    'workout_number': WorkoutNumber,
    'workout_programming_mode': WorkoutProgrammingMode,
    'display_update_rate': DisplayUpdateRate,
}

STROKE_ENUMS = {
    'stroke_state': StrokeState,
    'stroke_rate_state': StrokeRateState,
}

DISPLAY_ENUMS = {
    'display_units_type': DisplayUnitsType,
    'display_format_type': DisplayFormatType,
}

RACE_ENUMS = {
    'start_type': StartType,
    'race_operation_type': RaceOperationType,
    'race_state': RaceState,
    'race_type': RaceType,
    'race_start_state': RaceStartState,
    'status_type': StatusType,
}

# Combine all enum maps into one
ENUM_MAPS = {
    **MACHINE_ENUMS,
    **WORKOUT_ENUMS,
    **STROKE_ENUMS,
    **DISPLAY_ENUMS,
}

# ---------------------------------------------------------------------------------- #
# --- FUNCTIONS --- #
def get_enum_string(data_dict) -> dict:
    """
    Get the enum value from the enum class.
    """
    translated = {}
    for key, value in data_dict.items():
        enum_class = ENUM_MAPS.get(key)
        if enum_class:
            try:
                translated[key] = enum_class(value).name.replace('_', ' ')
            except ValueError:
                logging.warning(f'Invalid enum value {value} for key {key}')
                translated[key] = value
        else:
            logging.warning(f'No enum mapping for key: {key}')
            translated[key] = value

    return translated

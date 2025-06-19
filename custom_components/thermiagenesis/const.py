import pythermiagenesis.const as thermiaconst
from homeassistant.components.climate.const import ATTR_CURRENT_TEMPERATURE
from homeassistant.components.climate.const import ATTR_MAX_TEMP
from homeassistant.components.climate.const import ATTR_MIN_TEMP
from homeassistant.components.climate.const import ATTR_TARGET_TEMP_HIGH
from homeassistant.components.climate.const import ATTR_TARGET_TEMP_LOW
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import ATTR_TEMPERATURE
from homeassistant.const import PERCENTAGE
from homeassistant.const import UnitOfTemperature

ATTR_ICON = "icon"
ATTR_LABEL = "label"
ATTR_MANUFACTURER = "Thermia"
ATTR_MODEL = "Thermia Genesis"
ATTR_STATUS = "status"
ATTR_UNIT = "unit"
ATTR_CLASS = "device_class"
ATTR_STATE_CLASS = "state_class"
ATTR_UPTIME = "uptime"
ATTR_ENABLED = "enabled"
ATTR_DEFAULT_ENABLED = "default_enabled"
ATTR_SCALE = "scale"
ATTR_ADDR = "address"
ATTR_MAX_VALUE = "max_value"
ATTR_MIN_VALUE = "min_value"

ATTR_COUNTER = "counter"
ATTR_FIRMWARE = "firmware"

KEY_STATE_ATTRIBUTES = "state_attrs"
KEY_STATUS_VALUE = "status_value"

UNIT_RPM = "rpm"
UNIT_KELVIN = "K"
UNIT_SECONDS = "s"
UNIT_HOURS = "h"
UNIT_TEMPERATURE = UnitOfTemperature.CELSIUS
UNIT_VOLTAGE = "V"
UNIT_AMPERE = "A"
UNIT_WATT = "W"
UNIT_ENERGY = "kWh"


DOMAIN = "thermiagenesis"

MODEL_MEGA = "mega"
MODEL_INVERTER = "inverter"

ICON_DINPUT = "mdi-toggle-switch"
ICON_INPUT = "mdi-gauge"
ICON_COIL = "mdi-pencil"
ICON_HOLDING = "mdi-gauge"
CLASS_RELAY = "opening"
CLASS_ALARM = "problem"
CLASS_STATE = "plug"
CLASS_ENERGY = "energy"

ATTR_STATUS = thermiaconst.ATTR_INPUT_FIRST_PRIORITISED_DEMAND

HEATPUMP_SENSOR = thermiaconst.ATTR_INPUT_FIRST_PRIORITISED_DEMAND
HEATPUMP_ATTRIBUTES = [
    [thermiaconst.ATTR_INPUT_COMPRESSOR_SPEED_RPM, "rpm"],
    [thermiaconst.ATTR_INPUT_COMPRESSOR_CURRENT_GEAR, None],
    [thermiaconst.ATTR_INPUT_QUEUED_DEMAND_SECOND_PRIORITY, None],
    [thermiaconst.ATTR_INPUT_QUEUED_DEMAND_THIRD_PRIORITY, None],
    [thermiaconst.ATTR_INPUT_BRINE_IN_TEMPERATURE, UNIT_TEMPERATURE],
    [thermiaconst.ATTR_INPUT_BRINE_OUT_TEMPERATURE, UNIT_TEMPERATURE],
    [thermiaconst.ATTR_INPUT_COMPRESSOR_OPERATING_HOURS, UNIT_HOURS],
    [thermiaconst.ATTR_INPUT_TAP_WATER_OPERATING_HOURS, UNIT_HOURS],
    [thermiaconst.ATTR_INPUT_EXTERNAL_ADDITIONAL_HEATER_OPERATING_HOURS, UNIT_HOURS],
]
HEATPUMP_ALARMS = [
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_A,
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_B,
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_C,
]

CLIMATE_TYPES = {
    "tap_water": {
        ATTR_LABEL: "Tap water",
        ATTR_CURRENT_TEMPERATURE: thermiaconst.ATTR_INPUT_TAP_WATER_WEIGHTED_TEMPERATURE,
        ATTR_TARGET_TEMP_HIGH: thermiaconst.ATTR_HOLDING_STOP_TEMPERATURE_TAP_WATER,
        ATTR_TARGET_TEMP_LOW: thermiaconst.ATTR_HOLDING_START_TEMPERATURE_TAP_WATER,
        ATTR_MIN_TEMP: 35,
        ATTR_MAX_TEMP: 60,
        ATTR_ENABLED: thermiaconst.ATTR_COIL_ENABLE_TAP_WATER,
        ATTR_DEFAULT_ENABLED: True,
        KEY_STATUS_VALUE: "Hot water",
    },
    "pool": {
        ATTR_LABEL: "Pool",
        ATTR_CURRENT_TEMPERATURE: thermiaconst.ATTR_INPUT_POOL_RETURN_LINE_TEMPERATURE,
        ATTR_TEMPERATURE: thermiaconst.ATTR_HOLDING_SET_POINT_RETURN_TEMP_FROM_POOL_TO_HEAT_EXCHANGER,
        ATTR_MIN_TEMP: 10,
        ATTR_MAX_TEMP: 40,
        ATTR_ENABLED: thermiaconst.ATTR_COIL_ENABLE_POOL,
        ATTR_DEFAULT_ENABLED: True,
        KEY_STATUS_VALUE: "Pool",
    },
    "heat": {
        ATTR_LABEL: "Heat",
        # ATTR_CURRENT_TEMPERATURE: ATTR_INPUT_SYSTEM_SUPPLY_LINE_CALCULATED_SET_POINT,
        ATTR_CURRENT_TEMPERATURE: thermiaconst.ATTR_INPUT_ROOM_TEMPERATURE_SENSOR,
        ATTR_TEMPERATURE: thermiaconst.ATTR_HOLDING_COMFORT_WHEEL_SETTING,
        ATTR_MIN_TEMP: 10,
        ATTR_MAX_TEMP: 40,
        ATTR_ENABLED: thermiaconst.ATTR_COIL_ENABLE_HEAT,
        ATTR_DEFAULT_ENABLED: True,
        KEY_STATUS_VALUE: "Heat",
    },
}

SWITCH_TYPES = {
    thermiaconst.ATTR_COIL_RESET_ALL_ALARMS: {
        ATTR_LABEL: "Reset All Alarms",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_ADDITIONAL_HEATER: {
        ATTR_LABEL: "Enable Internal Additional Heater",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_EXTERNAL_ADDITIONAL_HEATER: {
        ATTR_LABEL: "Enable External Additional Heater",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_HGW: {
        ATTR_LABEL: "Enable HGW",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_FLOW_SWITCH_PRESSURE_SWITCH: {
        ATTR_LABEL: "Enable Flow Switch Pressure Switch",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_TAP_WATER: {
        ATTR_LABEL: "Enable Tap Water",
        ATTR_DEFAULT_ENABLED: True,
    },
    thermiaconst.ATTR_COIL_ENABLE_HEAT: {
        ATTR_LABEL: "Enable Heat",
        ATTR_DEFAULT_ENABLED: True,
    },
    thermiaconst.ATTR_COIL_ENABLE_ACTIVE_COOLING: {
        ATTR_LABEL: "Enable Active Cooling",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_MIX_VALVE_1: {
        ATTR_LABEL: "Enable Mix Valve 1",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_TWC: {
        ATTR_LABEL: "Enable TWC",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_WCS: {
        ATTR_LABEL: "Enable WCS",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_HOT_GAS_PUMP: {
        ATTR_LABEL: "Enable Hot Gas Pump",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_MIX_VALVE_2: {
        ATTR_LABEL: "Enable Mix Valve 2",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_MIX_VALVE_3: {
        ATTR_LABEL: "Enable Mix Valve 3",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_MIX_VALVE_4: {
        ATTR_LABEL: "Enable Mix Valve 4",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_MIX_VALVE_5: {
        ATTR_LABEL: "Enable Mix Valve 5",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_BRINE_OUT_MONITORING: {
        ATTR_LABEL: "Enable Brine Out Monitoring",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_BRINE_PUMP_CONTINUOUS_OPERATION: {
        ATTR_LABEL: "Enable Brine Pump Continuous Operation",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_SYSTEM_CIRCULATION_PUMP: {
        ATTR_LABEL: "Enable System Circulation Pump",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_DEW_POINT_CALCULATION: {
        ATTR_LABEL: "Enable Dew Point Calculation",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_ANTI_LEGIONELLA: {
        ATTR_LABEL: "Enable Anti Legionella",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_ADDITIONAL_HEATER_ONLY: {
        ATTR_LABEL: "Enable Additional Heater Only",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_CURRENT_LIMITATION: {
        ATTR_LABEL: "Enable Current Limitation",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_POOL: {
        ATTR_LABEL: "Enable Pool",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_SURPLUS_HEAT_CHILLER: {
        ATTR_LABEL: "Enable Surplus Heat Chiller",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_SURPLUS_HEAT_BOREHOLE: {
        ATTR_LABEL: "Enable Surplus Heat Borehole",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_EXTERNAL_ADDITIONAL_HEATER_FOR_POOL: {
        ATTR_LABEL: "Enable External Additional Heater For Pool",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_ADDITIONAL_HEATER_FOR_POOL: {
        ATTR_LABEL: "Enable Internal Additional Heater For Pool",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_PASSIVE_COOLING: {
        ATTR_LABEL: "Enable Passive Cooling",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_VARIABLE_SPEED_MODE_FOR_CONDENSER_PUMP: {
        ATTR_LABEL: "Enable Variable Speed Mode For Condenser Pump",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_VARIABLE_SPEED_MODE_FOR_BRINE_PUMP: {
        ATTR_LABEL: "Enable Variable Speed Mode For Brine Pump",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_COOLING_MODE_FOR_MIXING_VALVE_1: {
        ATTR_LABEL: "Enable Cooling Mode For Mixing Valve 1",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_COOLING_WITH_MIXING_VALVE_1: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Cooling With Mixing Valve 1",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_BRINE_PUMP_TO_START_WHEN_COOLING_IS_ACTIVE_FOR_MIXING_VALVE_1: {
        ATTR_LABEL: "Enable Internal Brine Pump To Start When Cooling Is Active For Mixing Valve 1",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_EXTERNAL_HEATER: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For External Heater",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_BRINE_IN_MONITORING: {
        ATTR_LABEL: "Enable Brine In Monitoring",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_FIXED_SYSTEM_SUPPLY_SET_POINT: {
        ATTR_LABEL: "Enable Fixed System Supply Set Point",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_EVAPORATOR_FREEZE_PROTECTION: {
        ATTR_LABEL: "Enable Evaporator Freeze Protection",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_COOLING_WITH_MIXING_VALVE_2: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Cooling With Mixing Valve 2",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_DEW_POINT_CALCULATION_ON_MIXING_VALVE_2: {
        ATTR_LABEL: "Enable Dew Point Calculation On Mixing Valve 2",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_HEATING_WITH_MIXING_VALVE_2: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Heating With Mixing Valve 2",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_COOLING_WITH_MIXING_VALVE_3: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Cooling With Mixing Valve 3",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_DEW_POINT_CALCULATION_ON_MIXING_VALVE_3: {
        ATTR_LABEL: "Enable Dew Point Calculation On Mixing Valve 3",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_HEATING_WITH_MIXING_VALVE_3: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Heating With Mixing Valve 3",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_COOLING_WITH_MIXING_VALVE_4: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Cooling With Mixing Valve 4",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_DEW_POINT_CALCULATION_ON_MIXING_VALVE_4: {
        ATTR_LABEL: "Enable Dew Point Calculation On Mixing Valve 4",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_HEATING_WITH_MIXING_VALVE_4: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Heating With Mixing Valve 4",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_COOLING_WITH_MIXING_VALVE_5: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Cooling With Mixing Valve 5",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_DEW_POINT_CALCULATION_ON_MIXING_VALVE_5: {
        ATTR_LABEL: "Enable Dew Point Calculation On Mixing Valve 5",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_OUTDOOR_TEMP_DEPENDENT_FOR_HEATING_WITH_MIXING_VALVE_5: {
        ATTR_LABEL: "Enable Outdoor Temp Dependent For Heating With Mixing Valve 5",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_BRINE_PUMP_TO_START_WHEN_COOLING_IS_ACTIVE_FOR_MIXING_VALVE_2: {
        ATTR_LABEL: "Enable Internal Brine Pump To Start When Cooling Is Active For Mixing Valve 2",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_BRINE_PUMP_TO_START_WHEN_COOLING_IS_ACTIVE_FOR_MIXING_VALVE_3: {
        ATTR_LABEL: "Enable Internal Brine Pump To Start When Cooling Is Active For Mixing Valve 3",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_BRINE_PUMP_TO_START_WHEN_COOLING_IS_ACTIVE_FOR_MIXING_VALVE_4: {
        ATTR_LABEL: "Enable Internal Brine Pump To Start When Cooling Is Active For Mixing Valve 4",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_COIL_ENABLE_INTERNAL_BRINE_PUMP_TO_START_WHEN_COOLING_IS_ACTIVE_FOR_MIXING_VALVE_5: {
        ATTR_LABEL: "Enable Internal Brine Pump To Start When Cooling Is Active For Mixing Valve 5",
        ATTR_DEFAULT_ENABLED: False,
    },
}

BINARY_SENSOR_TYPES = {
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_A: {
        ATTR_LABEL: "Alarm Active Class A",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_B: {
        ATTR_LABEL: "Alarm Active Class B",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_C: {
        ATTR_LABEL: "Alarm Active Class C",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_D: {
        ATTR_LABEL: "Alarm Active Class D",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_ALARM_ACTIVE_CLASS_E: {
        ATTR_LABEL: "Alarm Active Class E",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HIGH_PRESSURE_SWITCH_ALARM: {
        ATTR_LABEL: "High Pressure Switch Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_LOW_PRESSURE_LEVEL_ALARM: {
        ATTR_LABEL: "Low Pressure Level Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HIGH_DISCHARGE_PIPE_TEMPERATURE_ALARM: {
        ATTR_LABEL: "High Discharge Pipe Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_OPERATING_PRESSURE_LIMIT_INDICATION: {
        ATTR_LABEL: "Operating Pressure Limit Indication",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_DISCHARGE_PIPE_SENSOR_ALARM: {
        ATTR_LABEL: "Discharge Pipe Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_LIQUID_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Liquid Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SUCTION_GAS_SENSOR_ALARM: {
        ATTR_LABEL: "Suction Gas Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_FLOW_PRESSURE_SWITCH_ALARM: {
        ATTR_LABEL: "Flow Pressure Switch Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_POWER_INPUT_PHASE_DETECTION_ALARM: {
        ATTR_LABEL: "Power Input Phase Detection Alarm",
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_INVERTER_UNIT_ALARM: {
        ATTR_LABEL: "Inverter Unit Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SYSTEM_SUPPLY_LOW_TEMPERATURE_ALARM: {
        ATTR_LABEL: "System Supply Low Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COMPRESSOR_LOW_SPEED_ALARM: {
        ATTR_LABEL: "Compressor Low Speed Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_LOW_SUPER_HEAT_ALARM: {
        ATTR_LABEL: "Low Super Heat Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_PRESSURE_RATIO_OUT_OF_RANGE_ALARM: {
        ATTR_LABEL: "Pressure Ratio Out Of Range Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COMPRESSOR_PRESSURE_OUTSIDE_ENVELOPE_ALARM: {
        ATTR_LABEL: "Compressor Pressure Outside Envelope Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_TEMPERATURE_OUT_OF_RANGE_ALARM: {
        ATTR_LABEL: "Brine Temperature Out Of Range Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_IN_SENSOR_ALARM: {
        ATTR_LABEL: "Brine In Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_OUT_SENSOR_ALARM: {
        ATTR_LABEL: "Brine Out Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_CONDENSER_IN_SENSOR_ALARM: {
        ATTR_LABEL: "Condenser In Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_CONDENSER_OUT_SENSOR_ALARM: {
        ATTR_LABEL: "Condenser Out Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_OUTDOOR_SENSOR_ALARM: {
        ATTR_LABEL: "Outdoor Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SYSTEM_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "System Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_1_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Mix Valve 1 Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_2_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Mix Valve 2 Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_3_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Mix Valve 3 Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_4_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Mix Valve 4 Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_5_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Mix Valve 5 Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_WCS_RETURN_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Wcs Return Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Twc Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_TANK_SENSOR_ALARM: {
        ATTR_LABEL: "Cooling Tank Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Cooling Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_CIRCUIT_RETURN_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Cooling Circuit Return Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_DELTA_OUT_OF_RANGE_ALARM: {
        ATTR_LABEL: "Brine Delta Out Of Range Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TAP_WATER_MID_SENSOR_ALARM: {
        ATTR_LABEL: "Tap Water Mid Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_CIRCULATION_RETURN_SENSOR_ALARM: {
        ATTR_LABEL: "Twc Circulation Return Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HGW_SENSOR_ALARM: {
        ATTR_LABEL: "Hgw Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_INTERNAL_ADDITIONAL_HEATER_ALARM: {
        ATTR_LABEL: "Internal Additional Heater Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_IN_HIGH_TEMPERATURE_ALARM: {
        ATTR_LABEL: "Brine In High Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_IN_LOW_TEMPERATURE_ALARM: {
        ATTR_LABEL: "Brine In Low Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_OUT_LOW_TEMPERATURE_ALARM: {
        ATTR_LABEL: "Brine Out Low Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_CIRCULATION_RETURN_LOW_TEMPERATURE_ALARM: {
        ATTR_LABEL: "Twc Circulation Return Low Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_SUPPLY_LOW_TEMPERATURE_ALARM: {
        ATTR_LABEL: "Twc Supply Low Temperature Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_1_SUPPLY_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Mix Valve 1 Supply Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_2_SUPPLY_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Mix Valve 2 Supply Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_3_SUPPLY_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Mix Valve 3 Supply Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_4_SUPPLY_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Mix Valve 4 Supply Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_5_SUPPLY_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Mix Valve 5 Supply Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_WCS_RETURN_LINE_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Wcs Return Line Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SUM_ALARM: {
        ATTR_LABEL: "Sum Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_CIRCUIT_SUPPLY_LINE_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Cooling Circuit Supply Line Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_TANK_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Cooling Tank Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_TEMPERATURE_DEVIATION_ALARM: {
        ATTR_LABEL: "Surplus Heat Temperature Deviation Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HUMIDITY_ROOM_SENSOR_ALARM: {
        ATTR_LABEL: "Humidity Room Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_SUPPLY_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Surplus Heat Supply Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_RETURN_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Surplus Heat Return Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_TANK_RETURN_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Cooling Tank Return Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TEMPERATURE_ROOM_SENSOR_ALARM: {
        ATTR_LABEL: "Temperature Room Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_INVERTER_UNIT_COMMUNICATION_ALARM: {
        ATTR_LABEL: "Inverter Unit Communication Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_POOL_RETURN_LINE_SENSOR_ALARM: {
        ATTR_LABEL: "Pool Return Line Sensor Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_STOP_FOR_POOL: {
        ATTR_LABEL: "External Stop For Pool",
        ATTR_CLASS: CLASS_RELAY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_START_BRINE_PUMP: {
        ATTR_LABEL: "External Start Brine Pump",
        ATTR_CLASS: CLASS_RELAY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_RELAY_FOR_BRINE_GROUND_WATER_PUMP: {
        ATTR_LABEL: "External Relay For Brine Ground Water Pump",
        ATTR_CLASS: CLASS_RELAY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TAP_WATER_END_TANK_SENSOR_ALARM: {
        ATTR_LABEL: "Tap Water End Tank Sensor Alarm",
        ATTR_CLASS: CLASS_RELAY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MAXIMUM_TIME_FOR_ANTI_LEGIONELLA_EXCEEDED_ALARM: {
        ATTR_LABEL: "Maximum Time For Anti Legionella Exceeded Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_GENESIS_SECONDARY_UNIT_ALARM: {
        ATTR_LABEL: "Genesis Secondary Unit Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_PRIMARY_UNIT_CONFLICT_ALARM: {
        ATTR_LABEL: "Primary Unit Conflict Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_PRIMARY_UNIT_NO_SECONDARY_ALARM: {
        ATTR_LABEL: "Primary Unit No Secondary Alarm",
        ATTR_CLASS: CLASS_ALARM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_OIL_BOOST_IN_PROGRESS: {
        ATTR_LABEL: "Oil Boost In Progress",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COMPRESSOR_CONTROL_SIGNAL: {
        ATTR_LABEL: "Compressor Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SMART_GRID_1: {
        ATTR_LABEL: "Smart Grid 1",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_ALARM_INPUT: {
        ATTR_LABEL: "External Alarm Input",
        ATTR_CLASS: CLASS_RELAY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SMART_GRID_2: {
        ATTR_LABEL: "Smart Grid 2",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_ADDITIONAL_HEATER_CONTROL_SIGNAL: {
        ATTR_LABEL: "External Additional Heater Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_MIX_VALVE_1_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Mix Valve 1 Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_CONDENSER_PUMP_ON_OFF_CONTROL: {
        ATTR_LABEL: "Condenser Pump On Off Control",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SYSTEM_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "System Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HOT_GAS_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Hot Gas Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_BRINE_PUMP_ON_OFF_CONTROL: {
        ATTR_LABEL: "Brine Pump On Off Control",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_HEATER_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "External Heater Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HEATING_SEASON_ACTIVE: {
        ATTR_LABEL: "Heating Season Active",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_EXTERNAL_ADDITIONAL_HEATER_ACTIVE: {
        ATTR_LABEL: "External Additional Heater Active",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_INTERNAL_ADDITIONAL_HEATER_ACTIVE: {
        ATTR_LABEL: "Internal Additional Heater Active",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HGW_REGULATION_CONTROL_SIGNAL: {
        ATTR_LABEL: "Hgw Regulation Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HEAT_PUMP_STOPPING: {
        ATTR_LABEL: "Heat Pump Stopping",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_HEAT_PUMP_OK_TO_START: {
        ATTR_LABEL: "Heat Pump Ok To Start",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_SUPPLY_LINE_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Twc Supply Line Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_WCS_REGULATION_CONTROL_SIGNAL: {
        ATTR_LABEL: "Wcs Regulation Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_WCS_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Wcs Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_TWC_END_TANK_HEATER_CONTROL_SIGNAL: {
        ATTR_LABEL: "Twc End Tank Heater Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_POOL_DIRECTIONAL_VALVE_POSITION: {
        ATTR_LABEL: "Pool Directional Valve Position",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_CIRCUIT_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Cooling Circuit Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_POOL_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Pool Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_DIRECTIONAL_VALVE_POSITION: {
        ATTR_LABEL: "Surplus Heat Directional Valve Position",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_CIRCULATION_PUMP_CONTROL_SIGNAL: {
        ATTR_LABEL: "Surplus Heat Circulation Pump Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COOLING_CIRCUIT_REGULATION_CONTROL_SIGNAL: {
        ATTR_LABEL: "Cooling Circuit Regulation Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_SURPLUS_HEAT_REGULATION_CONTROL_SIGNAL: {
        ATTR_LABEL: "Surplus Heat Regulation Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_ACTIVE_COOLING_DIRECTIONAL_VALVE_POSITION: {
        ATTR_LABEL: "Active Cooling Directional Valve Position",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_PASSIVE_ACTIVE_COOLING_DIRECTIONAL_VALVE_POSITION: {
        ATTR_LABEL: "Passive Active Cooling Directional Valve Position",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_POOL_REGULATION_CONTROL_SIGNAL: {
        ATTR_LABEL: "Pool Regulation Control Signal",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_INDICATION_WHEN_MIXING_VALVE_1_IS_PRODUCING_PASSIVE_COOLING: {
        ATTR_LABEL: "Indication When Mixing Valve 1 Is Producing Passive Cooling",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_DINPUT_COMPRESSOR_IS_UNABLE_TO_SPEED_UP: {
        ATTR_LABEL: "Compressor Is Unable To Speed Up",
        ATTR_CLASS: CLASS_STATE,
        ATTR_DEFAULT_ENABLED: False,
    },
}

SENSOR_TYPES = {
    thermiaconst.ATTR_INPUT_FIRST_PRIORITISED_DEMAND: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "First Prioritised Demand",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_AVAILABLE_GEARS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Available Gears",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_SPEED_RPM: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Speed Rpm",
        ATTR_UNIT: UNIT_RPM,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_EXTERNAL_ADDITIONAL_HEATER_CURRENT_DEMAND: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "External Additional Heater Current Demand",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DISCHARGE_PIPE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Discharge Pipe Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_CONDENSER_IN_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser In Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_CONDENSER_OUT_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser Out Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BRINE_IN_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine In Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BRINE_OUT_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Out Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SYSTEM_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "System Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_OUTDOOR_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Outdoor Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TAP_WATER_TOP_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Tap Water Top Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TAP_WATER_LOWER_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Tap Water Lower Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TAP_WATER_WEIGHTED_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Tap Water Weighted Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SYSTEM_SUPPLY_LINE_CALCULATED_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "System Supply Line Calculated Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SELECTED_HEAT_CURVE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Selected Heat Curve",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_6: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 6",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEAT_CURVE_X_COORDINATE_7: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heat Curve X Coordinate 7",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_SEASON_INTEGRAL_VALUE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Season Integral Value",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_CONDENSER_CIRCULATION_PUMP_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser Circulation Pump Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_1_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 1 Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BUFFER_TANK_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Buffer Tank Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_1_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 1 Position",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BRINE_CIRCULATION_PUMP_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Circulation Pump Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HGW_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Hgw Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HOT_WATER_DIRECTIONAL_VALVE_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Hot Water Directional Valve Position",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_OPERATING_HOURS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Operating Hours",
        ATTR_UNIT: UNIT_HOURS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TAP_WATER_OPERATING_HOURS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Tap Water Operating Hours",
        ATTR_UNIT: UNIT_HOURS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_EXTERNAL_ADDITIONAL_HEATER_OPERATING_HOURS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "External Additional Heater Operating Hours",
        ATTR_UNIT: UNIT_HOURS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_SPEED_PERCENT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Speed Percent",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SECOND_PRIORITISED_DEMAND: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Second Prioritised Demand",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_THIRD_PRIORITISED_DEMAND: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Third Prioritised Demand",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SOFTWARE_VERSION_MAJOR: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Software Version Major",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SOFTWARE_VERSION_MINOR: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Software Version Minor",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SOFTWARE_VERSION_MICRO: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Software Version Micro",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_TEMPORARILY_BLOCKED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Temporarily Blocked",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMPRESSOR_CURRENT_GEAR: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Compressor Current Gear",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_QUEUED_DEMAND_FIRST_PRIORITY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Queued Demand First Priority",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_QUEUED_DEMAND_SECOND_PRIORITY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Queued Demand Second Priority",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_QUEUED_DEMAND_THIRD_PRIORITY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Queued Demand Third Priority",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_QUEUED_DEMAND_FOURTH_PRIORITY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Queued Demand Fourth Priority",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_QUEUED_DEMAND_FIFTH_PRIORITY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Queued Demand Fifth Priority",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_INTERNAL_ADDITIONAL_HEATER_CURRENT_STEP: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Internal Additional Heater Current Step",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BUFFER_TANK_CHARGE_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Buffer Tank Charge Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L1_CURRENT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L1 Current",
        ATTR_UNIT: UNIT_AMPERE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L2_CURRENT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L2 Current",
        ATTR_UNIT: UNIT_AMPERE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L3_CURRENT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L3 Current",
        ATTR_UNIT: UNIT_AMPERE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L1_0_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L1 0 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L2_0_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L2 0 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L3_0_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L3 0 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L1_L2_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L1 L2 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L2_L3_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L2 L3 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L3_L1_VOLTAGE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L3 L1 Voltage",
        ATTR_UNIT: UNIT_VOLTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L1_POWER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L1 Power",
        ATTR_UNIT: UNIT_WATT,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L2_POWER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L2 Power",
        ATTR_UNIT: UNIT_WATT,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_L3_POWER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter L3 Power",
        ATTR_UNIT: UNIT_WATT,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_METER_VALUE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter Meter Value",
        ATTR_UNIT: UNIT_ENERGY,
        ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COMFORT_MODE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Comfort Mode",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ELECTRIC_METER_KWH_TOTAL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Electric Meter Kwh Total",
        ATTR_UNIT: UNIT_ENERGY,
        ATTR_STATE_CLASS: SensorStateClass.TOTAL_INCREASING,
        ATTR_CLASS: CLASS_ENERGY,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_WCS_VALVE_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "WCS Valve Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TWC_VALVE_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Valve Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_2_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 2 Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_3_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 3 Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_4_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 4 Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_5_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 5 Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DEW_POINT_ROOM: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Dew Point Room",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_SUPPLY_LINE_MIX_VALVE_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Supply Line Mix Valve Position",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SURPLUS_HEAT_FAN_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Fan Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_POOL_SUPPLY_LINE_MIX_VALVE_POSITION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Supply Line Mix Valve Position",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TWC_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TWC_RETURN_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Return Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_WCS_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "WCS Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TWC_END_TANK_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC End Tank Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_2_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 2 Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_3_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 3 Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_4_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 4 Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_CIRCUIT_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Circuit Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_TANK_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Tank Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_TANK_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Tank Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_COOLING_CIRCUIT_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Circuit Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_5_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 5 Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_2_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 2 Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_3_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 3 Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_4_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 4 Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_5_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 5 Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SURPLUS_HEAT_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SURPLUS_HEAT_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_POOL_SUPPLY_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Supply Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_POOL_RETURN_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Return Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_ROOM_TEMPERATURE_SENSOR: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Room Temperature Sensor",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_BUBBLE_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Bubble Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DEW_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Dew Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SUPERHEAT_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Superheat Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SUB_COOLING_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Sub Cooling Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LOW_PRESSURE_SIDE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Low Pressure Side",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HIGH_PRESSURE_SIDE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "High Pressure Side",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LIQUID_LINE_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Liquid Line Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_SUCTION_GAS_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Suction Gas Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_HEATING_SEASON_INTEGRAL_VALUE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heating Season Integral Value",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_P_VALUE_FOR_GEAR_SHIFTING_AND_DEMAND_CALCULATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "P Value For Gear Shifting And Demand Calculation",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_I_VALUE_FOR_GEAR_SHIFTING_AND_DEMAND_CALCULATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "I Value For Gear Shifting And Demand Calculation",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_D_VALUE_FOR_GEAR_SHIFTING_AND_DEMAND_CALCULATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "D Value For Gear Shifting And Demand Calculation",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_I_VALUE_FOR_COMPRESSOR_ON_OFF_BUFFER_TANK: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "I Value For Compressor On Off Buffer Tank",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_P_VALUE_FOR_COMPRESSOR_ON_OFF_BUFFER_TANK: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "P Value For Compressor On Off Buffer Tank",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MIX_VALVE_COOLING_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve Cooling Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_GEAR_FOR_TAP_WATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Gear For Tap Water",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_GEAR_FOR_HEATING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Gear For Heating",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_GEAR_FOR_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Gear For Cooling",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_GEAR_FOR_POOL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Gear For Pool",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_NUMBER_OF_AVAILABLE_SECONDARIES_GENESIS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Number Of Available Secondaries Genesis",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_NUMBER_OF_AVAILABLE_SECONDARIES_LEGACY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Number Of Available Secondaries Legacy",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_TOTAL_DISTRIBUTED_GEARS_TO_ALL_UNITS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Total Distributed Gears To All Units",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_MAXIMUM_GEAR_OUT_OF_ALL_THE_CURRENTLY_REQUESTED_GEARS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Maximum Gear Out Of All The Currently Requested Gears",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_TEMPERATURE_DISTRIBUTION_CIRCUIT_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Temperature Distribution Circuit Mix Valve 1",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_TEMPERATURE_DISTRIBUTION_CIRCUIT_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Temperature Distribution Circuit Mix Valve 2",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_TEMPERATURE_DISTRIBUTION_CIRCUIT_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Temperature Distribution Circuit Mix Valve 3",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_TEMPERATURE_DISTRIBUTION_CIRCUIT_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Temperature Distribution Circuit Mix Valve 4",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DESIRED_TEMPERATURE_DISTRIBUTION_CIRCUIT_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Temperature Distribution Circuit Mix Valve 5",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_DISCONNECT_HOT_GAS_END_TANK: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Disconnect Hot Gas End Tank",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LEGACY_HEAT_PUMP_COMPRESSOR_RUNNING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Legacy Heat Pump Compressor Running",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LEGACY_HEAT_PUMP_REPORTING_ALARM: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Legacy Heat Pump Reporting Alarm",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LEGACY_HEAT_PUMP_START_SIGNAL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Legacy Heat Pump Start Signal",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_LEGACY_HEAT_PUMP_TAP_WATER_SIGNAL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Legacy Heat Pump Tap Water Signal",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_COMBINED_OUTPUT_OF_ALL_CLASS_D_ALARMS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Combined Output Of All Class D Alarms",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_PRIMARY_UNIT_HAS_LOST_COMMUNICATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Primary Unit Has Lost Communication",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_CLASS_A_ALARM_DETECTED_ON_THE_GENESIS_SECONDARY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Class A Alarm Detected On The Genesis Secondary",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_CLASS_B_ALARM_DETECTED_ON_THE_GENESIS_SECONDARY: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Class B Alarm Detected On The Genesis Secondary",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_COMBINED_OUTPUT_OF_ALL_CLASS_E_ALARMS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Combined Output Of All Class E Alarms",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_GENERAL_LEGACY_HEAT_PUMP_ALARM: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm General Legacy Heat Pump Alarm",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_INPUT_PRIMARY_UNIT_ALARM_PRIMARY_UNIT_CAN_NOT_COMMUNICATE_WITH_EXPANSION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Primary Unit Alarm Primary Unit Can Not Communicate With Expansion",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
}

NUMBER_TYPES = {
    thermiaconst.ATTR_HOLDING_OPERATIONAL_MODE: {
        # 1: OFF, 2: Standby, 3: ON/Auto
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Operational Mode",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 3,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_COMFORT_WHEEL_SETTING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Comfort Wheel Setting",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_6: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 6",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_HEAT_CURVE_Y_7: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Heat Curve Y 7",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_HEATING_SEASON_STOP_TEMPERATURE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Heating Season Stop Temperature",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_START_TEMPERATURE_TAP_WATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Start Temperature Tap Water",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_STOP_TEMPERATURE_TAP_WATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Stop Temperature Tap Water",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MINIMUM_ALLOWED_GEAR_IN_HEATING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Minimum Allowed Gear In Heating",
        ATTR_UNIT: None,
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAXIMUM_ALLOWED_GEAR_IN_HEATING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Maximum Allowed Gear In Heating",
        ATTR_UNIT: None,
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAXIMUM_ALLOWED_GEAR_IN_TAP_WATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Maximum Allowed Gear In Tap Water",
        ATTR_UNIT: None,
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MINIMUM_ALLOWED_GEAR_IN_TAP_WATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Minimum Allowed Gear In Tap Water",
        ATTR_UNIT: None,
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_COOLING_MIX_VALVE_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Mix Valve Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_MIX_VALVE_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Mix Valve Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_WCS_RETURN_LINE_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "WCS Return Line Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_MIX_VALVE_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Mix Valve Lowest Allowed Opening Degree",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_MIX_VALVE_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Mix Valve Highest Allowed Opening Degree",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_START_TEMPERATURE_IMMERSION_HEATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Start Temperature Immersion Heater",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_START_DELAY_IMMERSION_HEATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Start Delay Immersion Heater",
        ATTR_UNIT: UNIT_SECONDS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_TWC_STOP_TEMPERATURE_IMMERSION_HEATER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "TWC Stop Temperature Immersion Heater",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_WCS_MIX_VALVE_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "WCS Mix Valve Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_WCS_MIX_VALVE_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "WCS Mix Valve Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_2_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 2 Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_2_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 2 Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_3_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 3 Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_3_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 3 Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_4_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 4 Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_4_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 4 Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_5_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 5 Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIX_VALVE_5_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Mix Valve 5 Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_CHILLER_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Chiller Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_COOLING_SUPPLY_LINE_MIX_VALVE_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Supply Line Mix Valve Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_COOLING_SUPPLY_LINE_MIX_VALVE_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Cooling Supply Line Mix Valve Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_OPENING_DEGREE_FOR_STARTING_FAN_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Opening Degree For Starting Fan 1",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_OPENING_DEGREE_FOR_STARTING_FAN_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Opening Degree For Starting Fan 2",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_OPENING_DEGREE_FOR_STOPPING_FAN_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Opening Degree For Stopping Fan 1",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_OPENING_DEGREE_FOR_STOPPING_FAN_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Opening Degree For Stopping Fan 2",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SURPLUS_HEAT_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Surplus Heat Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_POOL_CHARGE_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Charge Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_POOL_MIX_VALVE_LOWEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Mix Valve Lowest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_POOL_MIX_VALVE_HIGHEST_ALLOWED_OPENING_DEGREE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Pool Mix Valve Highest Allowed Opening Degree",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_GEAR_SHIFT_DELAY_HEATING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Gear Shift Delay Heating",
        ATTR_UNIT: UNIT_SECONDS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_GEAR_SHIFT_DELAY_POOL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Gear Shift Delay Pool",
        ATTR_UNIT: UNIT_SECONDS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_GEAR_SHIFT_DELAY_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Gear Shift Delay Cooling",
        ATTR_UNIT: UNIT_SECONDS,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_IN_HIGH_ALARM_LIMIT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine In High Alarm Limit",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_IN_LOW_ALARM_LIMIT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine In Low Alarm Limit",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_OUT_LOW_ALARM_LIMIT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Out Low Alarm Limit",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_MAX_DELTA_LIMIT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Max Delta Limit",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_HOT_GAS_PUMP_START_TEMPERATURE_DISCHARGE_PIPE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Hot Gas Pump Start Temperature Discharge Pipe",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_HOT_GAS_PUMP_LOWER_STOP_LIMIT_TEMPERATURE_DISCHARGE_PIPE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Hot Gas Pump Lower Stop Limit Temperature Discharge Pipe",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_HOT_GAS_PUMP_UPPER_STOP_LIMIT_TEMPERATURE_DISCHARGE_PIPE: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Hot Gas Pump Upper Stop Limit Temperature Discharge Pipe",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_EXTERNAL_ADDITIONAL_HEATER_START: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "External Additional Heater Start",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_CONDENSER_PUMP_LOWEST_ALLOWED_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser Pump Lowest Allowed Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_PUMP_LOWEST_ALLOWED_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Pump Lowest Allowed Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_EXTERNAL_ADDITIONAL_HEATER_STOP: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "External Additional Heater Stop",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_CONDENSER_PUMP_HIGHEST_ALLOWED_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser Pump Highest Allowed Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_PUMP_HIGHEST_ALLOWED_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Pump Highest Allowed Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_CONDENSER_PUMP_STANDBY_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Condenser Pump Standby Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_BRINE_PUMP_STANDBY_SPEED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Brine Pump Standby Speed",
        ATTR_UNIT: PERCENTAGE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MINIMUM_ALLOWED_GEAR_IN_POOL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Minimum Allowed Gear In Pool",
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAXIMUM_ALLOWED_GEAR_IN_POOL: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Maximum Allowed Gear In Pool",
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MINIMUM_ALLOWED_GEAR_IN_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Minimum Allowed Gear In Cooling",
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAXIMUM_ALLOWED_GEAR_IN_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Maximum Allowed Gear In Cooling",
        ATTR_MIN_VALUE: 1,
        ATTR_MAX_VALUE: 9,
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_START_TEMP_FOR_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Start Temp For Cooling",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_STOP_TEMP_FOR_COOLING: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Stop Temp For Cooling",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation Set Point Curve Radiator Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation Set Point Curve Radiator Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_1_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 1 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_2_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 2 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_3_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 3 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_4_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 4 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_5_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 5 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_6_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 6 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_7_MIX_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 7 Mix Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_FIXED_SYSTEM_SUPPLY_SET_POINT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Fixed System Supply Set Point",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation Set Point Curve Radiator Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation Set Point Curve Radiator Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_1_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 1 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_2_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 2 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_3_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 3 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_4_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 4 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_5_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 5 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_6_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 6 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_7_MIX_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 7 Mix Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation Set Point Curve Radiator Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation Set Point Curve Radiator Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_1_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 1 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_2_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 2 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_3_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 3 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_4_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 4 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_5_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 5 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_6_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 6 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_7_MIX_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 7 Mix Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation Set Point Curve Radiator Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation Set Point Curve Radiator Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_1_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 1 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_2_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 2 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_3_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 3 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_4_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 4 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_5_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 5 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_6_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 6 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_7_MIX_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 7 Mix Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MIN_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Min Limitation Set Point Curve Radiator Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_MAX_LIMITATION_SET_POINT_CURVE_RADIATOR_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Max Limitation Set Point Curve Radiator Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_1_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 1 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_2_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 2 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_3_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 3 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_4_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 4 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_5_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 5 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_6_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 6 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_CURVE_Y_COORDINATE_7_MIX_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Curve Y Coordinate 7 Mix Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_RETURN_TEMP_FROM_POOL_TO_HEAT_EXCHANGER: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Return Temp From Pool To Heat Exchanger",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_POOL_HYSTERESIS: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Pool Hysteresis",
        ATTR_UNIT: UNIT_KELVIN,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_FOR_SUPPLY_LINE_TEMP_PASSIVE_COOLING_WITH_MIXING_VALVE_1: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point For Supply Line Temp Passive Cooling With Mixing Valve 1",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SET_POINT_MINIMUM_OUTDOOR_TEMP_WHEN_COOLING_IS_PERMITTED: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Set Point Minimum Outdoor Temp When Cooling Is Permitted",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_EXTERNAL_HEATER_OUTDOOR_TEMP_LIMIT: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "External Heater Outdoor Temp Limit",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SELECTED_MODE_FOR_MIXING_VALVE_2: {
        # 0:Heat, 1:Cool, 2:Auto
        ATTR_MIN_VALUE: 0,
        ATTR_MAX_VALUE: 2,
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Selected Mode For Mixing Valve 2",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_DESIRED_COOLING_TEMPERATURE_SETPOINT_MIXING_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Cooling Temperature Setpoint Mixing Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_COOLING_TEMPERATURE_OUTDOOR_MIXING_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Cooling Temperature Outdoor Mixing Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_HEATING_TEMPERATURE_OUTDOOR_MIXING_VALVE_2: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Heating Temperature Outdoor Mixing Valve 2",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SELECTED_MODE_FOR_MIXING_VALVE_3: {
        # 0:Heat, 1:Cool, 2:Auto
        ATTR_MIN_VALUE: 0,
        ATTR_MAX_VALUE: 2,
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Selected Mode For Mixing Valve 3",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_DESIRED_COOLING_TEMPERATURE_SETPOINT_MIXING_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Cooling Temperature Setpoint Mixing Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_COOLING_TEMPERATURE_OUTDOOR_MIXING_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Cooling Temperature Outdoor Mixing Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_HEATING_TEMPERATURE_OUTDOOR_MIXING_VALVE_3: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Heating Temperature Outdoor Mixing Valve 3",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SELECTED_MODE_FOR_MIXING_VALVE_4: {
        # 0:Heat, 1:Cool, 2:Auto
        ATTR_MIN_VALUE: 0,
        ATTR_MAX_VALUE: 2,
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Selected Mode For Mixing Valve 4",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_DESIRED_COOLING_TEMPERATURE_SETPOINT_MIXING_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Cooling Temperature Setpoint Mixing Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_COOLING_TEMPERATURE_OUTDOOR_MIXING_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Cooling Temperature Outdoor Mixing Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_HEATING_TEMPERATURE_OUTDOOR_TEMP_MIXING_VALVE_4: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Heating Temperature Outdoor Temp Mixing Valve 4",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SELECTED_MODE_FOR_MIXING_VALVE_5: {
        # 0:Heat, 1:Cool, 2:Auto
        ATTR_MIN_VALUE: 0,
        ATTR_MAX_VALUE: 2,
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Selected Mode For Mixing Valve 5",
        ATTR_UNIT: None,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_DESIRED_COOLING_TEMPERATURE_SETPOINT_MIXING_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Desired Cooling Temperature Setpoint Mixing Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_COOLING_TEMPERATURE_OUTDOOR_MIXING_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Cooling Temperature Outdoor Mixing Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
    thermiaconst.ATTR_HOLDING_SEASONAL_HEATING_TEMPERATURE_OUTDOOR_MIXING_VALVE_5: {
        ATTR_ICON: ICON_INPUT,
        ATTR_LABEL: "Seasonal Heating Temperature Outdoor Mixing Valve 5",
        ATTR_UNIT: UNIT_TEMPERATURE,
        ATTR_DEFAULT_ENABLED: False,
    },
}

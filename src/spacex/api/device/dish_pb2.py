# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacex/api/device/dish.proto
"""Generated protocol buffer code."""
# Third-Party Libraries
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# felddy Libraries
from spacex.api.device import (
    dish_config_pb2 as spacex_dot_api_dot_device_dot_dish__config__pb2,
)
from spacex.api.device import common_pb2 as spacex_dot_api_dot_device_dot_common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1cspacex/api/device/dish.proto\x12\x11SpaceX.API.Device\x1a\x1espacex/api/device/common.proto\x1a#spacex/api/device/dish_config.proto")\n\x0f\x44ishStowRequest\x12\x16\n\x06unstow\x18\x01 \x01(\x08R\x06unstow"\x12\n\x10\x44ishStowResponse"\x17\n\x15\x44ishGetContextRequest"\x95\x08\n\x16\x44ishGetContextResponse\x12>\n\x0b\x64\x65vice_info\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.DeviceInfoR\ndeviceInfo\x12\x41\n\x0c\x64\x65vice_state\x18\x07 \x01(\x0b\x32\x1e.SpaceX.API.Device.DeviceStateR\x0b\x64\x65viceState\x12\x31\n\x14obstruction_fraction\x18\x02 \x01(\x02R\x13obstructionFraction\x12.\n\x13obstruction_valid_s\x18\x03 \x01(\x02R\x11obstructionValidS\x12/\n\x13obstruction_current\x18\x0c \x01(\x08R\x12obstructionCurrent\x12\x17\n\x07\x63\x65ll_id\x18\x04 \x01(\rR\x06\x63\x65llId\x12\x1e\n\x0bpop_rack_id\x18\x05 \x01(\rR\tpopRackId\x12\x30\n\x14initial_satellite_id\x18\x08 \x01(\rR\x12initialSatelliteId\x12,\n\x12initial_gateway_id\x18\t \x01(\rR\x10initialGatewayId\x12$\n\x0eon_backup_beam\x18\n \x01(\x08R\x0conBackupBeam\x12-\n\x13seconds_to_slot_end\x18\x06 \x01(\x02R\x10secondsToSlotEnd\x12\x36\n\x17\x64\x65\x62ug_telemetry_enabled\x18\x0b \x01(\x08R\x15\x64\x65\x62ugTelemetryEnabled\x12;\n\x1bpop_ping_drop_rate_15s_mean\x18\r \x01(\x02R\x16popPingDropRate15sMean\x12=\n\x1cpop_ping_latency_ms_15s_mean\x18\x0e \x01(\x02R\x17popPingLatencyMs15sMean\x12>\n\x1cseconds_since_last_1s_outage\x18\x0f \x01(\x02R\x18secondsSinceLast1sOutage\x12>\n\x1cseconds_since_last_2s_outage\x18\x10 \x01(\x02R\x18secondsSinceLast2sOutage\x12>\n\x1cseconds_since_last_5s_outage\x18\x11 \x01(\x02R\x18secondsSinceLast5sOutage\x12@\n\x1dseconds_since_last_15s_outage\x18\x12 \x01(\x02R\x19secondsSinceLast15sOutage\x12@\n\x1dseconds_since_last_60s_outage\x18\x13 \x01(\x02R\x19secondsSinceLast60sOutage"\xef\x02\n\nDishOutage\x12\x39\n\x05\x63\x61use\x18\x01 \x01(\x0e\x32#.SpaceX.API.Device.DishOutage.CauseR\x05\x63\x61use\x12,\n\x12start_timestamp_ns\x18\x02 \x01(\x03R\x10startTimestampNs\x12\x1f\n\x0b\x64uration_ns\x18\x03 \x01(\x04R\ndurationNs\x12\x1d\n\ndid_switch\x18\x04 \x01(\x08R\tdidSwitch"\xb7\x01\n\x05\x43\x61use\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x42OOTING\x10\x01\x12\n\n\x06STOWED\x10\x02\x12\x14\n\x10THERMAL_SHUTDOWN\x10\x03\x12\x0f\n\x0bNO_SCHEDULE\x10\x04\x12\x0b\n\x07NO_SATS\x10\x05\x12\x0e\n\nOBSTRUCTED\x10\x06\x12\x0f\n\x0bNO_DOWNLINK\x10\x07\x12\x0c\n\x08NO_PINGS\x10\x08\x12\x15\n\x11\x41\x43TUATOR_ACTIVITY\x10\t\x12\x0e\n\nCABLE_TEST\x10\n"\xd8\x02\n\x16\x44ishGetHistoryResponse\x12\x18\n\x07\x63urrent\x18\x01 \x01(\x04R\x07\x63urrent\x12,\n\x12pop_ping_drop_rate\x18\xe9\x07 \x03(\x02R\x0fpopPingDropRate\x12.\n\x13pop_ping_latency_ms\x18\xea\x07 \x03(\x02R\x10popPingLatencyMs\x12\x37\n\x17\x64ownlink_throughput_bps\x18\xeb\x07 \x03(\x02R\x15\x64ownlinkThroughputBps\x12\x33\n\x15uplink_throughput_bps\x18\xec\x07 \x03(\x02R\x13uplinkThroughputBps\x12\x38\n\x07outages\x18\xf1\x07 \x03(\x0b\x32\x1d.SpaceX.API.Device.DishOutageR\x07outagesJ\x06\x08\xed\x07\x10\xee\x07J\x06\x08\xee\x07\x10\xef\x07J\x06\x08\xef\x07\x10\xf0\x07J\x06\x08\xf0\x07\x10\xf1\x07"\xd4\x07\n\x15\x44ishGetStatusResponse\x12>\n\x0b\x64\x65vice_info\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.DeviceInfoR\ndeviceInfo\x12\x41\n\x0c\x64\x65vice_state\x18\x02 \x01(\x0b\x32\x1e.SpaceX.API.Device.DeviceStateR\x0b\x64\x65viceState\x12\x36\n\x06\x61lerts\x18\xed\x07 \x01(\x0b\x32\x1d.SpaceX.API.Device.DishAlertsR\x06\x61lerts\x12\x36\n\x06outage\x18\xf6\x07 \x01(\x0b\x32\x1d.SpaceX.API.Device.DishOutageR\x06outage\x12=\n\tgps_stats\x18\xf7\x07 \x01(\x0b\x32\x1f.SpaceX.API.Device.DishGpsStatsR\x08gpsStats\x12\x43\n\x1eseconds_to_first_nonempty_slot\x18\xea\x07 \x01(\x02R\x1asecondsToFirstNonemptySlot\x12,\n\x12pop_ping_drop_rate\x18\xeb\x07 \x01(\x02R\x0fpopPingDropRate\x12\x37\n\x17\x64ownlink_throughput_bps\x18\xef\x07 \x01(\x02R\x15\x64ownlinkThroughputBps\x12\x33\n\x15uplink_throughput_bps\x18\xf0\x07 \x01(\x02R\x13uplinkThroughputBps\x12.\n\x13pop_ping_latency_ms\x18\xf1\x07 \x01(\x02R\x10popPingLatencyMs\x12U\n\x11obstruction_stats\x18\xec\x07 \x01(\x0b\x32\'.SpaceX.API.Device.DishObstructionStatsR\x10obstructionStats\x12&\n\x0estow_requested\x18\xf2\x07 \x01(\x08R\rstowRequested\x12\x33\n\x15\x62oresight_azimuth_deg\x18\xf3\x07 \x01(\x02R\x13\x62oresightAzimuthDeg\x12\x37\n\x17\x62oresight_elevation_deg\x18\xf4\x07 \x01(\x02R\x15\x62oresightElevationDeg\x12%\n\x0e\x65th_speed_mbps\x18\xf8\x07 \x01(\x05R\x0c\x65thSpeedMbps\x12L\n\x0emobility_class\x18\xf9\x07 \x01(\x0e\x32$.SpaceX.API.Device.UserMobilityClassR\rmobilityClassJ\x06\x08\xe9\x07\x10\xea\x07J\x06\x08\xee\x07\x10\xef\x07J\x06\x08\xf5\x07\x10\xf6\x07"\x1e\n\x1c\x44ishGetObstructionMapRequest"g\n\x1d\x44ishGetObstructionMapResponse\x12\x19\n\x08num_rows\x18\x01 \x01(\rR\x07numRows\x12\x19\n\x08num_cols\x18\x02 \x01(\rR\x07numCols\x12\x10\n\x03snr\x18\x03 \x03(\x02R\x03snr"\xff\x02\n\nDishAlerts\x12!\n\x0cmotors_stuck\x18\x01 \x01(\x08R\x0bmotorsStuck\x12)\n\x10thermal_throttle\x18\x03 \x01(\x08R\x0fthermalThrottle\x12)\n\x10thermal_shutdown\x18\x02 \x01(\x08R\x0fthermalShutdown\x12\x33\n\x16mast_not_near_vertical\x18\x05 \x01(\x08R\x13mastNotNearVertical\x12/\n\x13unexpected_location\x18\x04 \x01(\x08R\x12unexpectedLocation\x12\x30\n\x14slow_ethernet_speeds\x18\x06 \x01(\x08R\x12slowEthernetSpeeds\x12\x18\n\x07roaming\x18\x07 \x01(\x08R\x07roaming\x12\'\n\x0finstall_pending\x18\x08 \x01(\x08R\x0einstallPending\x12\x1d\n\nis_heating\x18\t \x01(\x08R\tisHeating"F\n\x0c\x44ishGpsStats\x12\x1b\n\tgps_valid\x18\x01 \x01(\x08R\x08gpsValid\x12\x19\n\x08gps_sats\x18\x02 \x01(\rR\x07gpsSats"\x81\x04\n\x14\x44ishObstructionStats\x12\x31\n\x14\x63urrently_obstructed\x18\x05 \x01(\x08R\x13\x63urrentlyObstructed\x12/\n\x13\x66raction_obstructed\x18\x01 \x01(\x02R\x12\x66ractionObstructed\x12\x17\n\x07valid_s\x18\x04 \x01(\x02R\x06validS\x12:\n\x19wedge_fraction_obstructed\x18\x02 \x03(\x02R\x17wedgeFractionObstructed\x12\x41\n\x1dwedge_abs_fraction_obstructed\x18\x03 \x03(\x02R\x1awedgeAbsFractionObstructed\x12N\n$avg_prolonged_obstruction_duration_s\x18\x06 \x01(\x02R avgProlongedObstructionDurationS\x12N\n$avg_prolonged_obstruction_interval_s\x18\x07 \x01(\x02R avgProlongedObstructionIntervalS\x12\x45\n\x1f\x61vg_prolonged_obstruction_valid\x18\x08 \x01(\x08R\x1c\x61vgProlongedObstructionValidJ\x06\x08\xee\x07\x10\xef\x07"T\n\x18\x44ishAuthenticateResponse\x12\x38\n\x04\x64ish\x18\x02 \x01(\x0b\x32$.SpaceX.API.Device.ChallengeResponseR\x04\x64ish"-\n\x0fSelfTestRequest\x12\x1a\n\x08\x64\x65tailed\x18\x01 \x01(\x08R\x08\x64\x65tailed"B\n\x10SelfTestResponse\x12\x16\n\x06passed\x18\x01 \x01(\x08R\x06passed\x12\x16\n\x06report\x18\x02 \x01(\tR\x06report"\x1a\n\x18StartDishSelfTestRequest"\x1b\n\x19StartDishSelfTestResponse"\x8f\x02\n\x12SetTestModeRequest\x12\x45\n\x07rf_mode\x18\x01 \x01(\x0e\x32,.SpaceX.API.Device.SetTestModeRequest.RfModeR\x06rfMode\x12\x39\n\x19\x64isable_loss_of_comm_fdir\x18\xe9\x07 \x01(\x08R\x15\x64isableLossOfCommFdir\x12\x33\n\x15\x65nable_rules_override\x18\xea\x07 \x01(\x08R\x13\x65nableRulesOverride"B\n\x06RfMode\x12\x06\n\x02RX\x10\x00\x12\x08\n\x04IDLE\x10\x01\x12\x06\n\x02TX\x10\x02\x12\x07\n\x03\x43\x41L\x10\x03\x12\x08\n\x04USER\x10\x04\x12\x0b\n\x06NORMAL\x10\xa4\x03"\x15\n\x13SetTestModeResponse"V\n\x14\x44ishSetConfigRequest\x12>\n\x0b\x64ish_config\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.DishConfigR\ndishConfig"f\n\x15\x44ishSetConfigResponse\x12M\n\x13updated_dish_config\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.DishConfigR\x11updatedDishConfig"\x16\n\x14\x44ishGetConfigRequest"W\n\x15\x44ishGetConfigResponse\x12>\n\x0b\x64ish_config\x18\x01 \x01(\x0b\x32\x1d.SpaceX.API.Device.DishConfigR\ndishConfig*<\n\x11UserMobilityClass\x12\x0e\n\nSTATIONARY\x10\x00\x12\x0b\n\x07NOMADIC\x10\x01\x12\n\n\x06MOBILE\x10\x02*C\n\tDishState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tCONNECTED\x10\x01\x12\r\n\tSEARCHING\x10\x02\x12\x0b\n\x07\x42OOTING\x10\x03\x42\x17Z\x15spacex.com/api/deviceb\x06proto3'
)

_USERMOBILITYCLASS = DESCRIPTOR.enum_types_by_name["UserMobilityClass"]
UserMobilityClass = enum_type_wrapper.EnumTypeWrapper(_USERMOBILITYCLASS)
_DISHSTATE = DESCRIPTOR.enum_types_by_name["DishState"]
DishState = enum_type_wrapper.EnumTypeWrapper(_DISHSTATE)
STATIONARY = 0
NOMADIC = 1
MOBILE = 2
UNKNOWN = 0
CONNECTED = 1
SEARCHING = 2
BOOTING = 3


_DISHSTOWREQUEST = DESCRIPTOR.message_types_by_name["DishStowRequest"]
_DISHSTOWRESPONSE = DESCRIPTOR.message_types_by_name["DishStowResponse"]
_DISHGETCONTEXTREQUEST = DESCRIPTOR.message_types_by_name["DishGetContextRequest"]
_DISHGETCONTEXTRESPONSE = DESCRIPTOR.message_types_by_name["DishGetContextResponse"]
_DISHOUTAGE = DESCRIPTOR.message_types_by_name["DishOutage"]
_DISHGETHISTORYRESPONSE = DESCRIPTOR.message_types_by_name["DishGetHistoryResponse"]
_DISHGETSTATUSRESPONSE = DESCRIPTOR.message_types_by_name["DishGetStatusResponse"]
_DISHGETOBSTRUCTIONMAPREQUEST = DESCRIPTOR.message_types_by_name[
    "DishGetObstructionMapRequest"
]
_DISHGETOBSTRUCTIONMAPRESPONSE = DESCRIPTOR.message_types_by_name[
    "DishGetObstructionMapResponse"
]
_DISHALERTS = DESCRIPTOR.message_types_by_name["DishAlerts"]
_DISHGPSSTATS = DESCRIPTOR.message_types_by_name["DishGpsStats"]
_DISHOBSTRUCTIONSTATS = DESCRIPTOR.message_types_by_name["DishObstructionStats"]
_DISHAUTHENTICATERESPONSE = DESCRIPTOR.message_types_by_name["DishAuthenticateResponse"]
_SELFTESTREQUEST = DESCRIPTOR.message_types_by_name["SelfTestRequest"]
_SELFTESTRESPONSE = DESCRIPTOR.message_types_by_name["SelfTestResponse"]
_STARTDISHSELFTESTREQUEST = DESCRIPTOR.message_types_by_name["StartDishSelfTestRequest"]
_STARTDISHSELFTESTRESPONSE = DESCRIPTOR.message_types_by_name[
    "StartDishSelfTestResponse"
]
_SETTESTMODEREQUEST = DESCRIPTOR.message_types_by_name["SetTestModeRequest"]
_SETTESTMODERESPONSE = DESCRIPTOR.message_types_by_name["SetTestModeResponse"]
_DISHSETCONFIGREQUEST = DESCRIPTOR.message_types_by_name["DishSetConfigRequest"]
_DISHSETCONFIGRESPONSE = DESCRIPTOR.message_types_by_name["DishSetConfigResponse"]
_DISHGETCONFIGREQUEST = DESCRIPTOR.message_types_by_name["DishGetConfigRequest"]
_DISHGETCONFIGRESPONSE = DESCRIPTOR.message_types_by_name["DishGetConfigResponse"]
_DISHOUTAGE_CAUSE = _DISHOUTAGE.enum_types_by_name["Cause"]
_SETTESTMODEREQUEST_RFMODE = _SETTESTMODEREQUEST.enum_types_by_name["RfMode"]
DishStowRequest = _reflection.GeneratedProtocolMessageType(
    "DishStowRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHSTOWREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishStowRequest)
    },
)
_sym_db.RegisterMessage(DishStowRequest)

DishStowResponse = _reflection.GeneratedProtocolMessageType(
    "DishStowResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHSTOWRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishStowResponse)
    },
)
_sym_db.RegisterMessage(DishStowResponse)

DishGetContextRequest = _reflection.GeneratedProtocolMessageType(
    "DishGetContextRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETCONTEXTREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetContextRequest)
    },
)
_sym_db.RegisterMessage(DishGetContextRequest)

DishGetContextResponse = _reflection.GeneratedProtocolMessageType(
    "DishGetContextResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETCONTEXTRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetContextResponse)
    },
)
_sym_db.RegisterMessage(DishGetContextResponse)

DishOutage = _reflection.GeneratedProtocolMessageType(
    "DishOutage",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHOUTAGE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishOutage)
    },
)
_sym_db.RegisterMessage(DishOutage)

DishGetHistoryResponse = _reflection.GeneratedProtocolMessageType(
    "DishGetHistoryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETHISTORYRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetHistoryResponse)
    },
)
_sym_db.RegisterMessage(DishGetHistoryResponse)

DishGetStatusResponse = _reflection.GeneratedProtocolMessageType(
    "DishGetStatusResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETSTATUSRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetStatusResponse)
    },
)
_sym_db.RegisterMessage(DishGetStatusResponse)

DishGetObstructionMapRequest = _reflection.GeneratedProtocolMessageType(
    "DishGetObstructionMapRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETOBSTRUCTIONMAPREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetObstructionMapRequest)
    },
)
_sym_db.RegisterMessage(DishGetObstructionMapRequest)

DishGetObstructionMapResponse = _reflection.GeneratedProtocolMessageType(
    "DishGetObstructionMapResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETOBSTRUCTIONMAPRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetObstructionMapResponse)
    },
)
_sym_db.RegisterMessage(DishGetObstructionMapResponse)

DishAlerts = _reflection.GeneratedProtocolMessageType(
    "DishAlerts",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHALERTS,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishAlerts)
    },
)
_sym_db.RegisterMessage(DishAlerts)

DishGpsStats = _reflection.GeneratedProtocolMessageType(
    "DishGpsStats",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGPSSTATS,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGpsStats)
    },
)
_sym_db.RegisterMessage(DishGpsStats)

DishObstructionStats = _reflection.GeneratedProtocolMessageType(
    "DishObstructionStats",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHOBSTRUCTIONSTATS,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishObstructionStats)
    },
)
_sym_db.RegisterMessage(DishObstructionStats)

DishAuthenticateResponse = _reflection.GeneratedProtocolMessageType(
    "DishAuthenticateResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHAUTHENTICATERESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishAuthenticateResponse)
    },
)
_sym_db.RegisterMessage(DishAuthenticateResponse)

SelfTestRequest = _reflection.GeneratedProtocolMessageType(
    "SelfTestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SELFTESTREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.SelfTestRequest)
    },
)
_sym_db.RegisterMessage(SelfTestRequest)

SelfTestResponse = _reflection.GeneratedProtocolMessageType(
    "SelfTestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SELFTESTRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.SelfTestResponse)
    },
)
_sym_db.RegisterMessage(SelfTestResponse)

StartDishSelfTestRequest = _reflection.GeneratedProtocolMessageType(
    "StartDishSelfTestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTDISHSELFTESTREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.StartDishSelfTestRequest)
    },
)
_sym_db.RegisterMessage(StartDishSelfTestRequest)

StartDishSelfTestResponse = _reflection.GeneratedProtocolMessageType(
    "StartDishSelfTestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _STARTDISHSELFTESTRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.StartDishSelfTestResponse)
    },
)
_sym_db.RegisterMessage(StartDishSelfTestResponse)

SetTestModeRequest = _reflection.GeneratedProtocolMessageType(
    "SetTestModeRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETTESTMODEREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.SetTestModeRequest)
    },
)
_sym_db.RegisterMessage(SetTestModeRequest)

SetTestModeResponse = _reflection.GeneratedProtocolMessageType(
    "SetTestModeResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETTESTMODERESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.SetTestModeResponse)
    },
)
_sym_db.RegisterMessage(SetTestModeResponse)

DishSetConfigRequest = _reflection.GeneratedProtocolMessageType(
    "DishSetConfigRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHSETCONFIGREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishSetConfigRequest)
    },
)
_sym_db.RegisterMessage(DishSetConfigRequest)

DishSetConfigResponse = _reflection.GeneratedProtocolMessageType(
    "DishSetConfigResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHSETCONFIGRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishSetConfigResponse)
    },
)
_sym_db.RegisterMessage(DishSetConfigResponse)

DishGetConfigRequest = _reflection.GeneratedProtocolMessageType(
    "DishGetConfigRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETCONFIGREQUEST,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetConfigRequest)
    },
)
_sym_db.RegisterMessage(DishGetConfigRequest)

DishGetConfigResponse = _reflection.GeneratedProtocolMessageType(
    "DishGetConfigResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _DISHGETCONFIGRESPONSE,
        "__module__": "spacex.api.device.dish_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.DishGetConfigResponse)
    },
)
_sym_db.RegisterMessage(DishGetConfigResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\025spacex.com/api/device"
    _USERMOBILITYCLASS._serialized_start = 4927
    _USERMOBILITYCLASS._serialized_end = 4987
    _DISHSTATE._serialized_start = 4989
    _DISHSTATE._serialized_end = 5056
    _DISHSTOWREQUEST._serialized_start = 120
    _DISHSTOWREQUEST._serialized_end = 161
    _DISHSTOWRESPONSE._serialized_start = 163
    _DISHSTOWRESPONSE._serialized_end = 181
    _DISHGETCONTEXTREQUEST._serialized_start = 183
    _DISHGETCONTEXTREQUEST._serialized_end = 206
    _DISHGETCONTEXTRESPONSE._serialized_start = 209
    _DISHGETCONTEXTRESPONSE._serialized_end = 1254
    _DISHOUTAGE._serialized_start = 1257
    _DISHOUTAGE._serialized_end = 1624
    _DISHOUTAGE_CAUSE._serialized_start = 1441
    _DISHOUTAGE_CAUSE._serialized_end = 1624
    _DISHGETHISTORYRESPONSE._serialized_start = 1627
    _DISHGETHISTORYRESPONSE._serialized_end = 1971
    _DISHGETSTATUSRESPONSE._serialized_start = 1974
    _DISHGETSTATUSRESPONSE._serialized_end = 2954
    _DISHGETOBSTRUCTIONMAPREQUEST._serialized_start = 2956
    _DISHGETOBSTRUCTIONMAPREQUEST._serialized_end = 2986
    _DISHGETOBSTRUCTIONMAPRESPONSE._serialized_start = 2988
    _DISHGETOBSTRUCTIONMAPRESPONSE._serialized_end = 3091
    _DISHALERTS._serialized_start = 3094
    _DISHALERTS._serialized_end = 3477
    _DISHGPSSTATS._serialized_start = 3479
    _DISHGPSSTATS._serialized_end = 3549
    _DISHOBSTRUCTIONSTATS._serialized_start = 3552
    _DISHOBSTRUCTIONSTATS._serialized_end = 4065
    _DISHAUTHENTICATERESPONSE._serialized_start = 4067
    _DISHAUTHENTICATERESPONSE._serialized_end = 4151
    _SELFTESTREQUEST._serialized_start = 4153
    _SELFTESTREQUEST._serialized_end = 4198
    _SELFTESTRESPONSE._serialized_start = 4200
    _SELFTESTRESPONSE._serialized_end = 4266
    _STARTDISHSELFTESTREQUEST._serialized_start = 4268
    _STARTDISHSELFTESTREQUEST._serialized_end = 4294
    _STARTDISHSELFTESTRESPONSE._serialized_start = 4296
    _STARTDISHSELFTESTRESPONSE._serialized_end = 4323
    _SETTESTMODEREQUEST._serialized_start = 4326
    _SETTESTMODEREQUEST._serialized_end = 4597
    _SETTESTMODEREQUEST_RFMODE._serialized_start = 4531
    _SETTESTMODEREQUEST_RFMODE._serialized_end = 4597
    _SETTESTMODERESPONSE._serialized_start = 4599
    _SETTESTMODERESPONSE._serialized_end = 4620
    _DISHSETCONFIGREQUEST._serialized_start = 4622
    _DISHSETCONFIGREQUEST._serialized_end = 4708
    _DISHSETCONFIGRESPONSE._serialized_start = 4710
    _DISHSETCONFIGRESPONSE._serialized_end = 4812
    _DISHGETCONFIGREQUEST._serialized_start = 4814
    _DISHGETCONFIGREQUEST._serialized_end = 4836
    _DISHGETCONFIGRESPONSE._serialized_start = 4838
    _DISHGETCONFIGRESPONSE._serialized_end = 4925
# @@protoc_insertion_point(module_scope)

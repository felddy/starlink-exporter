# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacex/api/device/transceiver.proto
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


# cisagov Libraries
from spacex.api.device import common_pb2 as spacex_dot_api_dot_device_dot_common__pb2
from spacex.api.device import dish_pb2 as spacex_dot_api_dot_device_dot_dish__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#spacex/api/device/transceiver.proto\x12\x11SpaceX.API.Device\x1a\x1espacex/api/device/common.proto\x1a\x1cspacex/api/device/dish.proto"P\n TransceiverIFLoopbackTestRequest\x12,\n\x12\x65nable_if_loopback\x18\x01 \x01(\x08R\x10\x65nableIfLoopback"\xc4\x01\n!TransceiverIFLoopbackTestResponse\x12*\n\x11\x62\x65r_loopback_test\x18\x01 \x01(\x02R\x0f\x62\x65rLoopbackTest\x12*\n\x11snr_loopback_test\x18\x02 \x01(\x02R\x0fsnrLoopbackTest\x12,\n\x12rssi_loopback_test\x18\x03 \x01(\x02R\x10rssiLoopbackTest\x12\x19\n\x08pll_lock\x18\x04 \x01(\x08R\x07pllLock"\x1d\n\x1bTransceiverGetStatusRequest"\xea\x04\n\x1cTransceiverGetStatusResponse\x12I\n\tmod_state\x18\x01 \x01(\x0e\x32,.SpaceX.API.Device.TransceiverModulatorStateR\x08modState\x12M\n\x0b\x64\x65mod_state\x18\x02 \x01(\x0e\x32,.SpaceX.API.Device.TransceiverModulatorStateR\ndemodState\x12\x42\n\x08tx_state\x18\x03 \x01(\x0e\x32\'.SpaceX.API.Device.TransceiverTxRxStateR\x07txState\x12\x42\n\x08rx_state\x18\x04 \x01(\x0e\x32\'.SpaceX.API.Device.TransceiverTxRxStateR\x07rxState\x12\x33\n\x05state\x18\xee\x07 \x01(\x0e\x32\x1c.SpaceX.API.Device.DishStateR\x05state\x12=\n\x06\x66\x61ults\x18\xef\x07 \x01(\x0b\x32$.SpaceX.API.Device.TransceiverFaultsR\x06\x66\x61ults\x12l\n\x17transmit_blanking_state\x18\xf0\x07 \x01(\x0e\x32\x33.SpaceX.API.Device.TransceiverTransmitBlankingStateR\x15transmitBlankingState\x12\'\n\x0fmodem_asic_temp\x18\xf1\x07 \x01(\x02R\rmodemAsicTemp\x12\x1d\n\ntx_if_temp\x18\xf2\x07 \x01(\x02R\x08txIfTemp"\xaa\x01\n\x11TransceiverFaults\x12:\n\x1aover_temp_modem_asic_fault\x18\x01 \x01(\x08R\x16overTempModemAsicFault\x12/\n\x14over_temp_pcba_fault\x18\x02 \x01(\x08R\x11overTempPcbaFault\x12(\n\x10\x64\x63_voltage_fault\x18\x03 \x01(\x08R\x0e\x64\x63VoltageFault" \n\x1eTransceiverGetTelemetryRequest"\xd9\n\n\x1fTransceiverGetTelemetryResponse\x12\x33\n\x15\x61ntenna_pointing_mode\x18\xe9\x07 \x01(\rR\x13\x61ntennaPointingMode\x12$\n\rantenna_pitch\x18\xea\x07 \x01(\x02R\x0c\x61ntennaPitch\x12"\n\x0c\x61ntenna_roll\x18\xeb\x07 \x01(\x02R\x0b\x61ntennaRoll\x12)\n\x10\x61ntenna_rx_theta\x18\xec\x07 \x01(\x02R\x0e\x61ntennaRxTheta\x12\x31\n\x14\x61ntenna_true_heading\x18\xed\x07 \x01(\x02R\x12\x61ntennaTrueHeading\x12\x1e\n\nrx_channel\x18\xee\x07 \x01(\rR\trxChannel\x12\'\n\x0f\x63urrent_cell_id\x18\xef\x07 \x01(\rR\rcurrentCellId\x12\x34\n\x16seconds_until_slot_end\x18\xf0\x07 \x01(\x02R\x13secondsUntilSlotEnd\x12-\n\x13wb_rssi_peak_mag_db\x18\xf1\x07 \x01(\x02R\x0fwbRssiPeakMagDb\x12,\n\x12pop_ping_drop_rate\x18\xf2\x07 \x01(\x02R\x0fpopPingDropRate\x12\x16\n\x06snr_db\x18\xf3\x07 \x01(\x02R\x05snrDb\x12"\n\rl1_snr_avg_db\x18\xf4\x07 \x01(\x02R\nl1SnrAvgDb\x12"\n\rl1_snr_min_db\x18\xf5\x07 \x01(\x02R\nl1SnrMinDb\x12"\n\rl1_snr_max_db\x18\xf6\x07 \x01(\x02R\nl1SnrMaxDb\x12+\n\x11lmac_satellite_id\x18\xf7\x07 \x01(\rR\x0flmacSatelliteId\x12/\n\x13target_satellite_id\x18\xf8\x07 \x01(\rR\x11targetSatelliteId\x12\x1c\n\tgrant_mcs\x18\xf9\x07 \x01(\rR\x08grantMcs\x12+\n\x11grant_symbols_avg\x18\xfa\x07 \x01(\x02R\x0fgrantSymbolsAvg\x12\x1c\n\tded_grant\x18\xfb\x07 \x01(\rR\x08\x64\x65\x64Grant\x12\x44\n\x1emobility_proactive_slot_change\x18\xfc\x07 \x01(\rR\x1bmobilityProactiveSlotChange\x12\x42\n\x1dmobility_reactive_slot_change\x18\xfd\x07 \x01(\rR\x1amobilityReactiveSlotChange\x12\x30\n\x14rfp_total_syn_failed\x18\xfe\x07 \x01(\rR\x11rfpTotalSynFailed\x12$\n\x0enum_out_of_seq\x18\xff\x07 \x01(\rR\x0bnumOutOfSeq\x12%\n\x0enum_ulmap_drop\x18\x80\x08 \x01(\rR\x0cnumUlmapDrop\x12>\n\x1b\x63urrent_seconds_of_schedule\x18\x81\x08 \x01(\x02R\x18\x63urrentSecondsOfSchedule\x12U\n(send_label_switch_to_ground_failed_calls\x18\x82\x08 \x01(\rR"sendLabelSwitchToGroundFailedCalls\x12%\n\x0e\x65ma_velocity_x\x18\x83\x08 \x01(\x01R\x0c\x65maVelocityX\x12%\n\x0e\x65ma_velocity_y\x18\x84\x08 \x01(\x01R\x0c\x65maVelocityY\x12%\n\x0e\x65ma_velocity_z\x18\x85\x08 \x01(\x01R\x0c\x65maVelocityZ\x12\x1d\n\nce_rssi_db\x18\x86\x08 \x01(\x02R\x08\x63\x65RssiDb*^\n\x19TransceiverModulatorState\x12\x14\n\x10MODSTATE_UNKNOWN\x10\x00\x12\x14\n\x10MODSTATE_ENABLED\x10\x01\x12\x15\n\x11MODSTATE_DISABLED\x10\x02*M\n\x14TransceiverTxRxState\x12\x10\n\x0cTXRX_UNKNOWN\x10\x00\x12\x10\n\x0cTXRX_ENABLED\x10\x01\x12\x11\n\rTXRX_DISABLED\x10\x02*S\n TransceiverTransmitBlankingState\x12\x0e\n\nTB_UNKNOWN\x10\x00\x12\x0e\n\nTB_ENABLED\x10\x01\x12\x0f\n\x0bTB_DISABLED\x10\x02\x42\x17Z\x15spacex.com/api/deviceb\x06proto3'
)

_TRANSCEIVERMODULATORSTATE = DESCRIPTOR.enum_types_by_name["TransceiverModulatorState"]
TransceiverModulatorState = enum_type_wrapper.EnumTypeWrapper(
    _TRANSCEIVERMODULATORSTATE
)
_TRANSCEIVERTXRXSTATE = DESCRIPTOR.enum_types_by_name["TransceiverTxRxState"]
TransceiverTxRxState = enum_type_wrapper.EnumTypeWrapper(_TRANSCEIVERTXRXSTATE)
_TRANSCEIVERTRANSMITBLANKINGSTATE = DESCRIPTOR.enum_types_by_name[
    "TransceiverTransmitBlankingState"
]
TransceiverTransmitBlankingState = enum_type_wrapper.EnumTypeWrapper(
    _TRANSCEIVERTRANSMITBLANKINGSTATE
)
MODSTATE_UNKNOWN = 0
MODSTATE_ENABLED = 1
MODSTATE_DISABLED = 2
TXRX_UNKNOWN = 0
TXRX_ENABLED = 1
TXRX_DISABLED = 2
TB_UNKNOWN = 0
TB_ENABLED = 1
TB_DISABLED = 2


_TRANSCEIVERIFLOOPBACKTESTREQUEST = DESCRIPTOR.message_types_by_name[
    "TransceiverIFLoopbackTestRequest"
]
_TRANSCEIVERIFLOOPBACKTESTRESPONSE = DESCRIPTOR.message_types_by_name[
    "TransceiverIFLoopbackTestResponse"
]
_TRANSCEIVERGETSTATUSREQUEST = DESCRIPTOR.message_types_by_name[
    "TransceiverGetStatusRequest"
]
_TRANSCEIVERGETSTATUSRESPONSE = DESCRIPTOR.message_types_by_name[
    "TransceiverGetStatusResponse"
]
_TRANSCEIVERFAULTS = DESCRIPTOR.message_types_by_name["TransceiverFaults"]
_TRANSCEIVERGETTELEMETRYREQUEST = DESCRIPTOR.message_types_by_name[
    "TransceiverGetTelemetryRequest"
]
_TRANSCEIVERGETTELEMETRYRESPONSE = DESCRIPTOR.message_types_by_name[
    "TransceiverGetTelemetryResponse"
]
TransceiverIFLoopbackTestRequest = _reflection.GeneratedProtocolMessageType(
    "TransceiverIFLoopbackTestRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERIFLOOPBACKTESTREQUEST,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverIFLoopbackTestRequest)
    },
)
_sym_db.RegisterMessage(TransceiverIFLoopbackTestRequest)

TransceiverIFLoopbackTestResponse = _reflection.GeneratedProtocolMessageType(
    "TransceiverIFLoopbackTestResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERIFLOOPBACKTESTRESPONSE,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverIFLoopbackTestResponse)
    },
)
_sym_db.RegisterMessage(TransceiverIFLoopbackTestResponse)

TransceiverGetStatusRequest = _reflection.GeneratedProtocolMessageType(
    "TransceiverGetStatusRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERGETSTATUSREQUEST,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverGetStatusRequest)
    },
)
_sym_db.RegisterMessage(TransceiverGetStatusRequest)

TransceiverGetStatusResponse = _reflection.GeneratedProtocolMessageType(
    "TransceiverGetStatusResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERGETSTATUSRESPONSE,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverGetStatusResponse)
    },
)
_sym_db.RegisterMessage(TransceiverGetStatusResponse)

TransceiverFaults = _reflection.GeneratedProtocolMessageType(
    "TransceiverFaults",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERFAULTS,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverFaults)
    },
)
_sym_db.RegisterMessage(TransceiverFaults)

TransceiverGetTelemetryRequest = _reflection.GeneratedProtocolMessageType(
    "TransceiverGetTelemetryRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERGETTELEMETRYREQUEST,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverGetTelemetryRequest)
    },
)
_sym_db.RegisterMessage(TransceiverGetTelemetryRequest)

TransceiverGetTelemetryResponse = _reflection.GeneratedProtocolMessageType(
    "TransceiverGetTelemetryResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCEIVERGETTELEMETRYRESPONSE,
        "__module__": "spacex.api.device.transceiver_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.TransceiverGetTelemetryResponse)
    },
)
_sym_db.RegisterMessage(TransceiverGetTelemetryResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\025spacex.com/api/device"
    _TRANSCEIVERMODULATORSTATE._serialized_start = 2632
    _TRANSCEIVERMODULATORSTATE._serialized_end = 2726
    _TRANSCEIVERTXRXSTATE._serialized_start = 2728
    _TRANSCEIVERTXRXSTATE._serialized_end = 2805
    _TRANSCEIVERTRANSMITBLANKINGSTATE._serialized_start = 2807
    _TRANSCEIVERTRANSMITBLANKINGSTATE._serialized_end = 2890
    _TRANSCEIVERIFLOOPBACKTESTREQUEST._serialized_start = 120
    _TRANSCEIVERIFLOOPBACKTESTREQUEST._serialized_end = 200
    _TRANSCEIVERIFLOOPBACKTESTRESPONSE._serialized_start = 203
    _TRANSCEIVERIFLOOPBACKTESTRESPONSE._serialized_end = 399
    _TRANSCEIVERGETSTATUSREQUEST._serialized_start = 401
    _TRANSCEIVERGETSTATUSREQUEST._serialized_end = 430
    _TRANSCEIVERGETSTATUSRESPONSE._serialized_start = 433
    _TRANSCEIVERGETSTATUSRESPONSE._serialized_end = 1051
    _TRANSCEIVERFAULTS._serialized_start = 1054
    _TRANSCEIVERFAULTS._serialized_end = 1224
    _TRANSCEIVERGETTELEMETRYREQUEST._serialized_start = 1226
    _TRANSCEIVERGETTELEMETRYREQUEST._serialized_end = 1258
    _TRANSCEIVERGETTELEMETRYRESPONSE._serialized_start = 1261
    _TRANSCEIVERGETTELEMETRYRESPONSE._serialized_end = 2630
# @@protoc_insertion_point(module_scope)

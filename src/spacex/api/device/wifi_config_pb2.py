# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacex/api/device/wifi_config.proto
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
from spacex.api.device import command_pb2 as spacex_dot_api_dot_device_dot_command__pb2
from spacex.api.device import common_pb2 as spacex_dot_api_dot_device_dot_common__pb2

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#spacex/api/device/wifi_config.proto\x12\x11SpaceX.API.Device\x1a\x1fspacex/api/device/command.proto\x1a\x1espacex/api/device/common.proto"\x82\x02\n\nMeshConfig\x12!\n\x0c\x64isplay_name\x18\x01 \x01(\tR\x0b\x64isplayName\x12,\n\x12\x61pply_display_name\x18\x02 \x01(\x08R\x10\x61pplyDisplayName\x12/\n\x04\x61uth\x18\x03 \x01(\x0e\x32\x1b.SpaceX.API.Device.MeshAuthR\x04\x61uth\x12\x1d\n\napply_auth\x18\x04 \x01(\x08R\tapplyAuth\x12%\n\x0elast_connected\x18\x05 \x01(\x03R\rlastConnected\x12 \n\x0bincarnation\x18\x07 \x01(\x04R\x0bincarnationJ\x04\x08\x06\x10\x07J\x04\x08\x08\x10\t"\xcf#\n\nWifiConfig\x12!\n\x0c\x63ountry_code\x18\x03 \x01(\tR\x0b\x63ountryCode\x12%\n\x0esetup_complete\x18\x07 \x01(\x08R\rsetupComplete\x12\x31\n\x14\x61pply_setup_complete\x18\xf2\x07 \x01(\x08R\x12\x61pplySetupComplete\x12\x18\n\x07version\x18\t \x01(\rR\x07version\x12\x1b\n\x07mac_wan\x18\x0c \x01(\tB\x02\x18\x01R\x06macWan\x12\x1b\n\x07mac_lan\x18\r \x01(\tB\x02\x18\x01R\x06macLan\x12!\n\x0c\x63hannel_2ghz\x18\x13 \x01(\rR\x0b\x63hannel2ghz\x12-\n\x12\x61pply_channel_2ghz\x18\xf5\x07 \x01(\x08R\x10\x61pplyChannel2ghz\x12!\n\x0c\x63hannel_5ghz\x18\x14 \x01(\rR\x0b\x63hannel5ghz\x12-\n\x12\x61pply_channel_5ghz\x18\xf6\x07 \x01(\x08R\x10\x61pplyChannel5ghz\x12Q\n\x0cmesh_configs\x18! \x03(\x0b\x32..SpaceX.API.Device.WifiConfig.MeshConfigsEntryR\x0bmeshConfigs\x12h\n\x14mesh_configs_updates\x18\xd9\x17 \x03(\x0b\x32\x35.SpaceX.API.Device.WifiConfig.MeshConfigsUpdatesEntryR\x12meshConfigsUpdates\x12-\n\x12\x61pply_mesh_configs\x18\x89\x08 \x01(\x08R\x10\x61pplyMeshConfigs\x12?\n\x0c\x64ynamic_keys\x18\x16 \x03(\x0b\x32\x1c.SpaceX.API.Device.PublicKeyR\x0b\x64ynamicKeys\x12,\n\x12\x61pply_dynamic_keys\x18\' \x01(\x08R\x10\x61pplyDynamicKeys\x12\x1f\n\x0bis_repeater\x18\x17 \x01(\x08R\nisRepeater\x12+\n\x11\x61pply_is_repeater\x18\x87\x08 \x01(\x08R\x0f\x61pplyIsRepeater\x12\x1f\n\x0bis_aviation\x18\x31 \x01(\x08R\nisAviation\x12+\n\x11\x61pply_is_aviation\x18\xa8\x08 \x01(\x08R\x0f\x61pplyIsAviation\x12\x1d\n\nboot_count\x18\x1a \x01(\x05R\tbootCount\x12\x30\n\x04\x62oot\x18\xb9\x17 \x01(\x0b\x32\x1b.SpaceX.API.Device.BootInfoR\x04\x62oot\x12 \n\x0bnameservers\x18\x1e \x03(\tR\x0bnameservers\x12,\n\x11\x61pply_nameservers\x18\x9e\x08 \x01(\x08R\x10\x61pplyNameservers\x12\x1f\n\x0b\x62ypass_mode\x18\x1f \x01(\x08R\nbypassMode\x12+\n\x11\x61pply_bypass_mode\x18\x9f\x08 \x01(\x08R\x0f\x61pplyBypassMode\x12\x1f\n\x0b\x64\x66s_enabled\x18* \x01(\x08R\ndfsEnabled\x12+\n\x11\x61pply_dfs_enabled\x18\xa2\x08 \x01(\x08R\x0f\x61pplyDfsEnabled\x12\x42\n\x08networks\x18\xcc\x08 \x03(\x0b\x32%.SpaceX.API.Device.WifiConfig.NetworkR\x08networks\x12&\n\x0e\x61pply_networks\x18\xcd\x08 \x01(\x08R\rapplyNetworks\x12%\n\x0cnetwork_name\x18\x01 \x01(\tB\x02\x18\x01R\x0bnetworkName\x12\x31\n\x12\x61pply_network_name\x18\xe9\x07 \x01(\x08\x42\x02\x18\x01R\x10\x61pplyNetworkName\x12-\n\x10network_password\x18\x02 \x01(\tB\x02\x18\x01R\x0fnetworkPassword\x12\x39\n\x16\x61pply_network_password\x18\xea\x07 \x01(\x08\x42\x02\x18\x01R\x14\x61pplyNetworkPassword\x12\x1d\n\x08lan_ipv4\x18\x05 \x01(\tB\x02\x18\x01R\x07lanIpv4\x12(\n\x0e\x61pply_lan_ipv4\x18% \x01(\x08\x42\x02\x18\x01R\x0c\x61pplyLanIpv4\x12O\n\rwifi_security\x18\n \x01(\x0e\x32&.SpaceX.API.Device.WifiConfig.SecurityB\x02\x18\x01R\x0cwifiSecurity\x12\x33\n\x13\x61pply_wifi_security\x18\xec\x07 \x01(\x08\x42\x02\x18\x01R\x11\x61pplyWifiSecurity\x12.\n\x11network_name_5ghz\x18\x0b \x01(\tB\x02\x18\x01R\x0fnetworkName5ghz\x12:\n\x17\x61pply_network_name_5ghz\x18\xed\x07 \x01(\x08\x42\x02\x18\x01R\x14\x61pplyNetworkName5ghz\x12*\n\x11\x65nable_remote_ssh\x18" \x01(\x08R\x0f\x65nableRemoteSsh\x12\x36\n\x17\x61pply_enable_remote_ssh\x18\xa1\x08 \x01(\x08R\x14\x61pplyEnableRemoteSsh\x12\x33\n\x16last_remote_ssh_access\x18# \x01(\x03R\x13lastRemoteSshAccess\x12 \n\x0bincarnation\x18+ \x01(\x04R\x0bincarnation\x12X\n\x12wireless_mode_2ghz\x18, \x01(\x0e\x32*.SpaceX.API.Device.WifiConfig.WirelessModeR\x10wirelessMode2ghz\x12\x38\n\x18\x61pply_wireless_mode_2ghz\x18\xa3\x08 \x01(\x08R\x15\x61pplyWirelessMode2ghz\x12X\n\x12wireless_mode_5ghz\x18- \x01(\x0e\x32*.SpaceX.API.Device.WifiConfig.WirelessModeR\x10wirelessMode5ghz\x12\x38\n\x18\x61pply_wireless_mode_5ghz\x18\xa4\x08 \x01(\x08R\x15\x61pplyWirelessMode5ghz\x12U\n\x11ht_bandwidth_2ghz\x18. \x01(\x0e\x32).SpaceX.API.Device.WifiConfig.HTBandwidthR\x0fhtBandwidth2ghz\x12\x36\n\x17\x61pply_ht_bandwidth_2ghz\x18\xa5\x08 \x01(\x08R\x14\x61pplyHtBandwidth2ghz\x12U\n\x11ht_bandwidth_5ghz\x18/ \x01(\x0e\x32).SpaceX.API.Device.WifiConfig.HTBandwidthR\x0fhtBandwidth5ghz\x12\x36\n\x17\x61pply_ht_bandwidth_5ghz\x18\xa6\x08 \x01(\x08R\x14\x61pplyHtBandwidth5ghz\x12O\n\rvht_bandwidth\x18\x30 \x01(\x0e\x32*.SpaceX.API.Device.WifiConfig.VHTBandwidthR\x0cvhtBandwidth\x12/\n\x13\x61pply_vht_bandwidth\x18\xa7\x08 \x01(\x08R\x11\x61pplyVhtBandwidth\x1a]\n\x10MeshConfigsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.SpaceX.API.Device.MeshConfigR\x05value:\x02\x38\x01\x1a\x64\n\x17MeshConfigsUpdatesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x1d.SpaceX.API.Device.MeshConfigR\x05value:\x02\x38\x01\x1a\xbe\x04\n\x0f\x42\x61sicServiceSet\x12\x15\n\x05\x62ssid\x18\xeb\x07 \x01(\tR\x05\x62ssid\x12\x13\n\x04ssid\x18\xed\x07 \x01(\tR\x04ssid\x12;\n\tauth_open\x18\xd1\x0f \x01(\x0b\x32\x1b.SpaceX.API.Device.AuthOpenH\x00R\x08\x61uthOpen\x12;\n\tauth_wpa2\x18\xd2\x0f \x01(\x0b\x32\x1b.SpaceX.API.Device.AuthWpa2H\x00R\x08\x61uthWpa2\x12;\n\tauth_wpa3\x18\xd3\x0f \x01(\x0b\x32\x1b.SpaceX.API.Device.AuthWpa3H\x00R\x08\x61uthWpa3\x12H\n\x0e\x61uth_wpa2_wpa3\x18\xd4\x0f \x01(\x0b\x32\x1f.SpaceX.API.Device.AuthWpa2Wpa3H\x00R\x0c\x61uthWpa2Wpa3\x12\x41\n\x0b\x61uth_radius\x18\xd5\x0f \x01(\x0b\x32\x1d.SpaceX.API.Device.AuthRadiusH\x00R\nauthRadius\x12\x37\n\x04\x62\x61nd\x18\xf3\x07 \x01(\x0e\x32".SpaceX.API.Device.WifiConfig.BandR\x04\x62\x61nd\x12\x19\n\x07\x64isable\x18\xf5\x07 \x01(\x08R\x07\x64isable\x12\x17\n\x06hidden\x18\xf7\x07 \x01(\x08R\x06hiddenB\x06\n\x04\x61uthJ\x06\x08\xe8\x07\x10\xe9\x07J\x06\x08\xe9\x07\x10\xea\x07J\x06\x08\xea\x07\x10\xeb\x07J\x06\x08\xec\x07\x10\xed\x07J\x06\x08\xee\x07\x10\xef\x07J\x06\x08\xd0\x0f\x10\xd1\x0fJ\x06\x08\xf4\x07\x10\xf5\x07J\x06\x08\xf6\x07\x10\xf7\x07J\x06\x08\xf8\x07\x10\xf9\x07\x1a\xac\x01\n\x07Network\x12\x13\n\x04ipv4\x18\xeb\x07 \x01(\tR\x04ipv4\x12\\\n\x12\x62\x61sic_service_sets\x18\xef\x07 \x03(\x0b\x32-.SpaceX.API.Device.WifiConfig.BasicServiceSetR\x10\x62\x61sicServiceSetsJ\x06\x08\xe8\x07\x10\xe9\x07J\x06\x08\xe9\x07\x10\xea\x07J\x06\x08\xea\x07\x10\xeb\x07J\x06\x08\xec\x07\x10\xed\x07J\x06\x08\xed\x07\x10\xee\x07J\x06\x08\xee\x07\x10\xef\x07"9\n\x08Security\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04WPA2\x10\x01\x12\x08\n\x04WPA3\x10\x02\x12\x0c\n\x08WPA2WPA3\x10\x03"0\n\x04\x42\x61nd\x12\x0e\n\nRF_UNKNOWN\x10\x00\x12\x0b\n\x07RF_2GHZ\x10\x02\x12\x0b\n\x07RF_5GHZ\x10\x05"\xe5\x01\n\x0cWirelessMode\x12\x19\n\x15WIRELESS_MODE_DEFAULT\x10\x00\x12\n\n\x06\x41_ONLY\x10\x01\x12\n\n\x06\x42_ONLY\x10\x02\x12\n\n\x06G_ONLY\x10\x03\x12\n\n\x06N_ONLY\x10\x04\x12\r\n\tB_G_MIXED\x10\x05\x12\r\n\tA_N_MIXED\x10\x06\x12\r\n\tG_N_MIXED\x10\x07\x12\x0f\n\x0b\x42_G_N_MIXED\x10\x08\x12\x11\n\rA_AN_AC_MIXED\x10\t\x12\x0f\n\x0b\x41N_AC_MIXED\x10\n\x12\x12\n\x0e\x42_G_N_AX_MIXED\x10\x0b\x12\x14\n\x10\x41_AN_AC_AX_MIXED\x10\x0c"_\n\x0bHTBandwidth\x12\x18\n\x14HT_BANDWIDTH_DEFAULT\x10\x00\x12\x17\n\x13HT_BANDWIDTH_20_MHZ\x10\x01\x12\x1d\n\x19HT_BANDWIDTH_20_OR_40_MHZ\x10\x02"\x9c\x01\n\x0cVHTBandwidth\x12\x19\n\x15VHT_BANDWIDTH_DEFAULT\x10\x00\x12\x1a\n\x16VHT_BANDWIDTH_DISABLED\x10\x01\x12\x18\n\x14VHT_BANDWIDTH_80_MHZ\x10\x02\x12\x19\n\x15VHT_BANDWIDTH_160_MHZ\x10\x03\x12 \n\x1cVHT_BANDWIDTH_80_PLUS_80_MHZ\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x06\x10\x07J\x04\x08\x08\x10\tJ\x04\x08\x0e\x10\x0fJ\x04\x08\x0f\x10\x10J\x04\x08\x10\x10\x11J\x04\x08\x11\x10\x12J\x04\x08\x12\x10\x13J\x04\x08\x15\x10\x16J\x04\x08\x18\x10\x19J\x04\x08\x19\x10\x1aJ\x04\x08\x1b\x10\x1cJ\x04\x08\x1c\x10\x1dJ\x04\x08\x1d\x10\x1eJ\x04\x08 \x10!J\x04\x08$\x10%J\x04\x08&\x10\'J\x04\x08(\x10)J\x04\x08)\x10*J\x06\x08\xeb\x07\x10\xec\x07J\x06\x08\xee\x07\x10\xef\x07J\x06\x08\xef\x07\x10\xf0\x07J\x06\x08\xf0\x07\x10\xf1\x07J\x06\x08\xf1\x07\x10\xf2\x07J\x06\x08\xf3\x07\x10\xf4\x07J\x06\x08\xf4\x07\x10\xf5\x07J\x06\x08\xf7\x07\x10\xf8\x07J\x06\x08\xfd\x07\x10\xfe\x07J\x06\x08\x91\x08\x10\x92\x08J\x06\x08\x9b\x08\x10\x9c\x08J\x06\x08\x9c\x08\x10\x9d\x08J\x06\x08\x9d\x08\x10\x9e\x08J\x06\x08\xa0\x08\x10\xa1\x08J\x06\x08\xd1\x0f\x10\xd2\x0fJ\x06\x08\xd2\x0f\x10\xd3\x0fJ\x06\x08\xd3\x0f\x10\xd4\x0fJ\x06\x08\xd4\x0f\x10\xd5\x0fJ\x06\x08\xd5\x0f\x10\xd6\x0fJ\x06\x08\xd6\x0f\x10\xd7\x0fJ\x06\x08\xd7\x0f\x10\xd8\x0fJ\x06\x08\xd8\x0f\x10\xd9\x0f"\n\n\x08\x41uthOpen"&\n\x08\x41uthWpa2\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password"&\n\x08\x41uthWpa3\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password"*\n\x0c\x41uthWpa2Wpa3\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password"]\n\nAuthRadius\x12\x16\n\x06server\x18\x01 \x01(\tR\x06server\x12\x1b\n\tserver_ca\x18\x03 \x01(\tR\x08serverCa\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password*d\n\x08MeshAuth\x12\x15\n\x11MESH_AUTH_UNKNOWN\x10\x00\x12\x11\n\rMESH_AUTH_NEW\x10\x01\x12\x15\n\x11MESH_AUTH_TRUSTED\x10\x02\x12\x17\n\x13MESH_AUTH_UNTRUSTED\x10\x03\x42\x17Z\x15spacex.com/api/deviceb\x06proto3'
)

_MESHAUTH = DESCRIPTOR.enum_types_by_name["MeshAuth"]
MeshAuth = enum_type_wrapper.EnumTypeWrapper(_MESHAUTH)
MESH_AUTH_UNKNOWN = 0
MESH_AUTH_NEW = 1
MESH_AUTH_TRUSTED = 2
MESH_AUTH_UNTRUSTED = 3


_MESHCONFIG = DESCRIPTOR.message_types_by_name["MeshConfig"]
_WIFICONFIG = DESCRIPTOR.message_types_by_name["WifiConfig"]
_WIFICONFIG_MESHCONFIGSENTRY = _WIFICONFIG.nested_types_by_name["MeshConfigsEntry"]
_WIFICONFIG_MESHCONFIGSUPDATESENTRY = _WIFICONFIG.nested_types_by_name[
    "MeshConfigsUpdatesEntry"
]
_WIFICONFIG_BASICSERVICESET = _WIFICONFIG.nested_types_by_name["BasicServiceSet"]
_WIFICONFIG_NETWORK = _WIFICONFIG.nested_types_by_name["Network"]
_AUTHOPEN = DESCRIPTOR.message_types_by_name["AuthOpen"]
_AUTHWPA2 = DESCRIPTOR.message_types_by_name["AuthWpa2"]
_AUTHWPA3 = DESCRIPTOR.message_types_by_name["AuthWpa3"]
_AUTHWPA2WPA3 = DESCRIPTOR.message_types_by_name["AuthWpa2Wpa3"]
_AUTHRADIUS = DESCRIPTOR.message_types_by_name["AuthRadius"]
_WIFICONFIG_SECURITY = _WIFICONFIG.enum_types_by_name["Security"]
_WIFICONFIG_BAND = _WIFICONFIG.enum_types_by_name["Band"]
_WIFICONFIG_WIRELESSMODE = _WIFICONFIG.enum_types_by_name["WirelessMode"]
_WIFICONFIG_HTBANDWIDTH = _WIFICONFIG.enum_types_by_name["HTBandwidth"]
_WIFICONFIG_VHTBANDWIDTH = _WIFICONFIG.enum_types_by_name["VHTBandwidth"]
MeshConfig = _reflection.GeneratedProtocolMessageType(
    "MeshConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _MESHCONFIG,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.MeshConfig)
    },
)
_sym_db.RegisterMessage(MeshConfig)

WifiConfig = _reflection.GeneratedProtocolMessageType(
    "WifiConfig",
    (_message.Message,),
    {
        "MeshConfigsEntry": _reflection.GeneratedProtocolMessageType(
            "MeshConfigsEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WIFICONFIG_MESHCONFIGSENTRY,
                "__module__": "spacex.api.device.wifi_config_pb2"
                # @@protoc_insertion_point(class_scope:SpaceX.API.Device.WifiConfig.MeshConfigsEntry)
            },
        ),
        "MeshConfigsUpdatesEntry": _reflection.GeneratedProtocolMessageType(
            "MeshConfigsUpdatesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _WIFICONFIG_MESHCONFIGSUPDATESENTRY,
                "__module__": "spacex.api.device.wifi_config_pb2"
                # @@protoc_insertion_point(class_scope:SpaceX.API.Device.WifiConfig.MeshConfigsUpdatesEntry)
            },
        ),
        "BasicServiceSet": _reflection.GeneratedProtocolMessageType(
            "BasicServiceSet",
            (_message.Message,),
            {
                "DESCRIPTOR": _WIFICONFIG_BASICSERVICESET,
                "__module__": "spacex.api.device.wifi_config_pb2"
                # @@protoc_insertion_point(class_scope:SpaceX.API.Device.WifiConfig.BasicServiceSet)
            },
        ),
        "Network": _reflection.GeneratedProtocolMessageType(
            "Network",
            (_message.Message,),
            {
                "DESCRIPTOR": _WIFICONFIG_NETWORK,
                "__module__": "spacex.api.device.wifi_config_pb2"
                # @@protoc_insertion_point(class_scope:SpaceX.API.Device.WifiConfig.Network)
            },
        ),
        "DESCRIPTOR": _WIFICONFIG,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.WifiConfig)
    },
)
_sym_db.RegisterMessage(WifiConfig)
_sym_db.RegisterMessage(WifiConfig.MeshConfigsEntry)
_sym_db.RegisterMessage(WifiConfig.MeshConfigsUpdatesEntry)
_sym_db.RegisterMessage(WifiConfig.BasicServiceSet)
_sym_db.RegisterMessage(WifiConfig.Network)

AuthOpen = _reflection.GeneratedProtocolMessageType(
    "AuthOpen",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHOPEN,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthOpen)
    },
)
_sym_db.RegisterMessage(AuthOpen)

AuthWpa2 = _reflection.GeneratedProtocolMessageType(
    "AuthWpa2",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHWPA2,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthWpa2)
    },
)
_sym_db.RegisterMessage(AuthWpa2)

AuthWpa3 = _reflection.GeneratedProtocolMessageType(
    "AuthWpa3",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHWPA3,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthWpa3)
    },
)
_sym_db.RegisterMessage(AuthWpa3)

AuthWpa2Wpa3 = _reflection.GeneratedProtocolMessageType(
    "AuthWpa2Wpa3",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHWPA2WPA3,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthWpa2Wpa3)
    },
)
_sym_db.RegisterMessage(AuthWpa2Wpa3)

AuthRadius = _reflection.GeneratedProtocolMessageType(
    "AuthRadius",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHRADIUS,
        "__module__": "spacex.api.device.wifi_config_pb2"
        # @@protoc_insertion_point(class_scope:SpaceX.API.Device.AuthRadius)
    },
)
_sym_db.RegisterMessage(AuthRadius)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"Z\025spacex.com/api/device"
    _WIFICONFIG_MESHCONFIGSENTRY._options = None
    _WIFICONFIG_MESHCONFIGSENTRY._serialized_options = b"8\001"
    _WIFICONFIG_MESHCONFIGSUPDATESENTRY._options = None
    _WIFICONFIG_MESHCONFIGSUPDATESENTRY._serialized_options = b"8\001"
    _WIFICONFIG.fields_by_name["mac_wan"]._options = None
    _WIFICONFIG.fields_by_name["mac_wan"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["mac_lan"]._options = None
    _WIFICONFIG.fields_by_name["mac_lan"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["network_name"]._options = None
    _WIFICONFIG.fields_by_name["network_name"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["apply_network_name"]._options = None
    _WIFICONFIG.fields_by_name["apply_network_name"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["network_password"]._options = None
    _WIFICONFIG.fields_by_name["network_password"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["apply_network_password"]._options = None
    _WIFICONFIG.fields_by_name[
        "apply_network_password"
    ]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["lan_ipv4"]._options = None
    _WIFICONFIG.fields_by_name["lan_ipv4"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["apply_lan_ipv4"]._options = None
    _WIFICONFIG.fields_by_name["apply_lan_ipv4"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["wifi_security"]._options = None
    _WIFICONFIG.fields_by_name["wifi_security"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["apply_wifi_security"]._options = None
    _WIFICONFIG.fields_by_name["apply_wifi_security"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["network_name_5ghz"]._options = None
    _WIFICONFIG.fields_by_name["network_name_5ghz"]._serialized_options = b"\030\001"
    _WIFICONFIG.fields_by_name["apply_network_name_5ghz"]._options = None
    _WIFICONFIG.fields_by_name[
        "apply_network_name_5ghz"
    ]._serialized_options = b"\030\001"
    _MESHAUTH._serialized_start = 5177
    _MESHAUTH._serialized_end = 5277
    _MESHCONFIG._serialized_start = 124
    _MESHCONFIG._serialized_end = 382
    _WIFICONFIG._serialized_start = 385
    _WIFICONFIG._serialized_end = 4944
    _WIFICONFIG_MESHCONFIGSENTRY._serialized_start = 3110
    _WIFICONFIG_MESHCONFIGSENTRY._serialized_end = 3203
    _WIFICONFIG_MESHCONFIGSUPDATESENTRY._serialized_start = 3205
    _WIFICONFIG_MESHCONFIGSUPDATESENTRY._serialized_end = 3305
    _WIFICONFIG_BASICSERVICESET._serialized_start = 3308
    _WIFICONFIG_BASICSERVICESET._serialized_end = 3882
    _WIFICONFIG_NETWORK._serialized_start = 3885
    _WIFICONFIG_NETWORK._serialized_end = 4057
    _WIFICONFIG_SECURITY._serialized_start = 4059
    _WIFICONFIG_SECURITY._serialized_end = 4116
    _WIFICONFIG_BAND._serialized_start = 4118
    _WIFICONFIG_BAND._serialized_end = 4166
    _WIFICONFIG_WIRELESSMODE._serialized_start = 4169
    _WIFICONFIG_WIRELESSMODE._serialized_end = 4398
    _WIFICONFIG_HTBANDWIDTH._serialized_start = 4400
    _WIFICONFIG_HTBANDWIDTH._serialized_end = 4495
    _WIFICONFIG_VHTBANDWIDTH._serialized_start = 4498
    _WIFICONFIG_VHTBANDWIDTH._serialized_end = 4654
    _AUTHOPEN._serialized_start = 4946
    _AUTHOPEN._serialized_end = 4956
    _AUTHWPA2._serialized_start = 4958
    _AUTHWPA2._serialized_end = 4996
    _AUTHWPA3._serialized_start = 4998
    _AUTHWPA3._serialized_end = 5036
    _AUTHWPA2WPA3._serialized_start = 5038
    _AUTHWPA2WPA3._serialized_end = 5080
    _AUTHRADIUS._serialized_start = 5082
    _AUTHRADIUS._serialized_end = 5175
# @@protoc_insertion_point(module_scope)

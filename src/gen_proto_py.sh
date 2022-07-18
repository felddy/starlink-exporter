#!/bin/bash

# This script will generate the Python source files from the Starlink Dish gRPC reflection.

set -o nounset
set -o errexit
set -o pipefail

GEN_DIR="."
PROTOSET=$(mktemp)

# An array of required commands
required_commands=(grpcurl)

# Verify that the required commands are installed
for command in "${required_commands[@]}"; do
  command -v "$command" > /dev/null 2>&1 || {
    echo "Error: $command is not installed. Please install it." >&2
    exit 1
  }
done

# Generate a protoset by using reflection on Dishy
grpcurl -plaintext -protoset-out "${PROTOSET}" 192.168.100.1:9200 describe SpaceX.API.Device.Device

mkdir -p ${GEN_DIR}

# Array of proto files in the protoset
proto_files=(
  spacex/api/common/status/status.proto
  spacex/api/device/command.proto
  spacex/api/device/common.proto
  spacex/api/device/device.proto
  spacex/api/device/dish_config.proto
  spacex/api/device/dish.proto
  spacex/api/device/transceiver.proto
  spacex/api/device/wifi_config.proto
  spacex/api/device/wifi.proto
)

# Gererate Python source for each proto file
for proto_file in "${proto_files[@]}"; do
  python3 -m grpc_tools.protoc --descriptor_set_in="${PROTOSET}" \
    --python_out="${GEN_DIR}" --grpc_python_out="${GEN_DIR}" "${proto_file}"
done

# Remove unneeded protoset
rm "${PROTOSET}"

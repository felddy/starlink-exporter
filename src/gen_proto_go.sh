#!/bin/bash

# This script will generate the go source files from the Starlink Disk gRPC reflection.

set -o nounset
set -o errexit
set -o pipefail

GEN_DIR="pkg"
PROTOSET=$(mktemp)

# An array of required commands
required_commands=(grpcurl protoc protoc-gen-go protoc-gen-go-grpc)

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

# Generate go files from protoset
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/common/status/status.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/command.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/common.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/device.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/dish_config.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/dish.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/transceiver.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/wifi_config.proto
protoc --descriptor_set_in="${PROTOSET}" --go_out="${GEN_DIR}" --go-grpc_out="${GEN_DIR}" spacex/api/device/wifi.proto

# Find all go files and replace import path with import path in this project
find "${GEN_DIR}" -name "*.go" -exec sed -i '' -e 's|spacex.com/api|github.com/felddy/starlink-exporter/pkg/spacex.com/api|g' {} \;

# Remove unneeded protoset
rm "${PROTOSET}"

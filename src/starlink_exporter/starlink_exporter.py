"""A Prometheus exporter for the Starlink dish.

Connects to a Starlink dish and presents the data as Prometheus metrics.

EXIT STATUS
    This utility exits with one of the following values:
    0   Completed successfully.
    >0  An error occurred.

Usage:
  starlink-exporter [--log-level=LEVEL] [options]
  starlink-exporter (-h | --help)

Options:
  -h --help                   Show this message.
  -p --port=PORT              Port to listen on [default: 9817].
  -d --dish-address=ADDRESS   The address of the dish
                              [default: 192.168.100.1:9200].
  --log-level=LEVEL           If specified, then the log level will be set to
                              the specified value.  Valid values are "debug",
                              "info", "warning", "error", and "critical".
                              [default: info]
"""

# Standard Python Libraries
import logging
import sys
from typing import Any, Dict

# Third-Party Libraries
import docopt
import grpc
from prometheus_client import CollectorRegistry, start_http_server
from schema import And, Schema, SchemaError, Use

# felddy Libraries
# Generated Libraries
import spacex.api.device.device_pb2 as pb2
from spacex.api.device.device_pb2_grpc import DeviceStub

# Project imports
from ._version import __version__
from .collector import CustomCollector


def run(listen_port: int, dish_address: str) -> None:
    """Connect to the dish using gRPC and print out the device info."""

    registry = CollectorRegistry()

    # TODO handle connection errors
    with grpc.insecure_channel(dish_address) as channel:
        dish_client = DeviceStub(channel)

        status = dish_client.Handle(pb2.Request(get_status={}), timeout=10)
        # history = client.Handle(pb2.Request(get_history={}), timeout=10)
        # obstruction_map = client.Handle(
        #     pb2.Request(dish_get_obstruction_map={}), timeout=10
        # )

        logging.info(f"Device id: f{status.dish_get_status.device_info.id}")
        logging.info(
            f"Software version: f{status.dish_get_status.device_info.software_version}"
        )
        logging.info(
            f"Hardware version: f{status.dish_get_status.device_info.hardware_version}"
        )

        # Create custom collector
        logging.debug("Creating custom collector.")
        collector = CustomCollector(dish_client)
        registry.register(collector)

        logging.info(f"Starting http server on port {listen_port}")
        start_http_server(listen_port, registry=registry)

        # Drop into an IPython shell
        # Third-Party Libraries
        import IPython

        IPython.embed(colors="neutral")


def main() -> None:
    """Set up logging and call the example function."""
    args: Dict[str, str] = docopt.docopt(__doc__, version=__version__)
    # Validate and convert arguments as needed
    schema: Schema = Schema(
        {
            "--dish-address": And(
                str,
                lambda n: len(n.split(":")) == 2,
                error="--dish-address must be of the form <host>:<port>.",
            ),
            "--port": And(
                Use(int),
                lambda n: n > 0 and n < 65536,
                error="--port must be an integer between 1 and 65535 inclusive.",
            ),
            "--log-level": And(
                str,
                Use(str.lower),
                lambda n: n in ("debug", "info", "warning", "error", "critical"),
                error="Possible values for --log-level are "
                + "debug, info, warning, error, and critical.",
            ),
            str: object,  # Don't care about other keys, if any
        }
    )

    try:
        validated_args: Dict[str, Any] = schema.validate(args)
    except SchemaError as err:
        # Exit because one or more of the arguments were invalid
        print(err, file=sys.stderr)
        sys.exit(1)

    # Assign validated arguments to variables
    dish_address: str = validated_args["--dish-address"]
    log_level: str = validated_args["--log-level"]
    port: int = validated_args["--port"]

    # Set up logging
    logging.basicConfig(
        format="%(asctime)-15s %(levelname)s %(message)s", level=log_level.upper()
    )

    logging.debug("Starting Starlink exporter with the following arguments:")
    logging.debug(f"  dish address: {dish_address}")
    logging.debug(f"  server port: {port}")

    run(port, dish_address)

    # Stop logging and clean up
    logging.shutdown()

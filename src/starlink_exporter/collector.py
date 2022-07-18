# Standard Python Libraries
from typing import Generator

# Third-Party Libraries
import grpc
from prometheus_client import Gauge
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily, Metric

# felddy Libraries
import spacex.api.device.device_pb2 as pb2

from . import TIMEOUT


class CustomCollector(object):
    """Custom Prometheus collector for Starlink dish."""

    # Initialize with dish client
    def __init__(self, dish_client):
        self.dish_client = dish_client

    def collect(self) -> Generator[Metric, None, None]:
        try:
            status = self.dish_client.Handle(
                pb2.Request(get_status={}), timeout=TIMEOUT
            )
            yield GaugeMetricFamily(
                "starlink_dish_up",
                "Was the last query of Starlink dish successful.",
                value=True,
            )
            yield from self.__collect_device_info(status.dish_get_status.device_info)
            yield from self.__collect_gps_stats(status.dish_get_status.gps_stats)
            yield from self.__collect_obstructions(
                status.dish_get_status.obstruction_stats
            )
            # self.collect_alerts()
            # self.collect_obstructions()
            # self.collect_history()
        except grpc.RpcError as rpc_error:
            print(rpc_error)
            yield GaugeMetricFamily(
                "starlink_dish_up",
                "Was the last query of Starlink dish successful.",
                value=False,
            )

    def __collect_obstructions(
        self, obstruction_stats
    ) -> Generator[Metric, None, None]:
        """Create a gauge with values for each obstruction name."""
        yield GaugeMetricFamily(
            "fraction_obstructed",
            "Percentage of absolute obstruction per wedge section",
            value=obstruction_stats.fraction_obstructed,
        )
        yield GaugeMetricFamily(
            "valid_s",  # TODO figure out what this is
            "Validity of the obstruction map in seconds",
            value=obstruction_stats.valid_s,
        )
        yield GaugeMetricFamily(
            "avg_prolonged_obstruction_duration_s",
            "Average duration of prolonged obstructions in seconds",
            value=obstruction_stats.avg_prolonged_obstruction_duration_s,
        )
        yield GaugeMetricFamily(
            "avg_prolonged_obstruction_interval_s",
            "Average interval between prolonged obstructions in seconds",
            value=obstruction_stats.avg_prolonged_obstruction_interval_s,
        )
        c = GaugeMetricFamily(
            "starlink_dish_wedge_abs_fraction_obstruction_ratio",
            "Percentage of absolute obstruction per wedge section",
            labels=["wedge", "wedge_name"],
        )
        for i, obs in enumerate(obstruction_stats.wedge_abs_fraction_obstructed):
            c.add_metric([str(i), f"{i*30}_{i*30+30}"], obs)
        yield c
        c = GaugeMetricFamily(
            "starlink_dish_wedge_fraction_obstruction_ratio",
            "Percentage of obstruction per wedge section",
            labels=["wedge", "wedge_name"],
        )
        for i, obs in enumerate(obstruction_stats.wedge_fraction_obstructed):
            c.add_metric([str(i), f"{i*30}_{i*30+30}"], obs)
        yield c

    def __collect_device_info(self, device_info) -> Generator[Metric, None, None]:
        """Collect device information."""
        c = GaugeMetricFamily(
            "device_info",
            "Device information",
            labels=[
                "bootcount",
                "country_code",
                "hardware_version",
                "id",
                "software_version",
                "utc_offset_s",
            ],
        )
        c.add_metric(
            [
                str(device_info.bootcount),
                device_info.country_code,
                device_info.hardware_version,
                device_info.id,
                device_info.software_version,
                str(device_info.utc_offset_s),
            ],
            1,
        )
        yield c

    def __collect_gps_stats(self, gps_stats) -> Generator[Metric, None, None]:
        """Collect status metrics."""
        # Print status
        yield GaugeMetricFamily(
            "gps_valid",
            "GPS location is valid",
            value=gps_stats.gps_valid,
        )
        yield GaugeMetricFamily(
            "gps_sats",
            "GPS satellites in view",
            value=gps_stats.gps_sats,
        )

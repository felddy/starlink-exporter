# Standard Python Libraries
from random import random
from typing import Generator

# Third-Party Libraries
import grpc
from prometheus_client import Gauge
from prometheus_client.core import CounterMetricFamily, GaugeMetricFamily, Metric

# felddy Libraries
import spacex.api.device.device_pb2 as pb2

from . import TIMEOUT

starlink_dish_up = GaugeMetricFamily("starlink_dish_up", "Dish is up", registry=None)


class CustomCollector(object):
    """Custom Prometheus collector for Starlink dish."""

    # Initialize with dish client
    def __init__(self, dish_client):
        self.dish_client = dish_client

    def collect(self) -> Generator[Metric, None, None]:
        try:
            for i in self.__collect_status():
                yield i
            # self.collect_alerts()
            # self.collect_obstructions()
            # self.collect_history()
            yield GaugeMetricFamily(
                "starlink_dish_up",
                "Was the last query of Starlink dish successful.",
                value=True,
            )
        except grpc.RpcError as rpc_error:
            print(rpc_error)
            yield GaugeMetricFamily(
                "starlink_dish_up",
                "Was the last query of Starlink dish successful.",
                value=False,
            )

    def __collect_status(self) -> Generator[Metric, None, None]:
        """Collect status metrics."""
        status = self.dish_client.Handle(pb2.Request(get_status={}), timeout=TIMEOUT)
        yield GaugeMetricFamily("my_gauge", "Help text", value=7)
        c = CounterMetricFamily("my_counter_total", "Help text", labels=["foo"])
        c.add_metric(["bar"], 1.7)
        c.add_metric(["baz"], random() * 4)
        yield c

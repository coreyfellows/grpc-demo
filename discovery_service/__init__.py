from .grpc_gen.discovery_service_pb2 import add_DiscoveryServiceServicer_to_server
from .service import DiscoveryService, start_up
from functools import partial
add_to_server = partial(add_DiscoveryServiceServicer_to_server, DiscoveryService())
name = "discovery_service"
discoverable = False

def initialize():
    start_up()
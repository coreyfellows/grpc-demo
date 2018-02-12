from .grpc_gen.merch_service_pb2_grpc import add_MerchServiceServicer_to_server
from .service import MerchService, start_up
from functools import partial
add_to_server = partial(add_MerchServiceServicer_to_server, MerchService())
name = "merch_service"
discoverable = True

def initialize():
    start_up()
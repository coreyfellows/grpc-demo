from .grpc_gen.%SERVICE_NAME%_pb2_grpc import add_%SERVICE_NAME_CAMEL_CASE%Servicer_to_server
from .service import %SERVICE_NAME_CAMEL_CASE%, start_up
from functools import partial
add_to_server = partial(add_%SERVICE_NAME_CAMEL_CASE%Servicer_to_server, %SERVICE_NAME_CAMEL_CASE%())
name = "%SERVICE_NAME%"
discoverable = True

def initialize():
    start_up()
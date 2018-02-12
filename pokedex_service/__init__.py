from .grpc_gen.pokedex_service_pb2_grpc import add_PokedexServiceServicer_to_server
from .service import PokedexService, start_up
from functools import partial
add_to_server = partial(add_PokedexServiceServicer_to_server, PokedexService())
name = "pokedex_service"
discoverable = True

def initialize():
    start_up()
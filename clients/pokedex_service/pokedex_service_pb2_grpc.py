# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

try:
    import pokedex_service_pb2 as pokedex__service__pb2
except:
    from . import pokedex_service_pb2 as pokedex__service__pb2


class PokedexServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetPokemon = channel.unary_unary(
        '/PokedexService/GetPokemon',
        request_serializer=pokedex__service__pb2.GetPokemon_Request.SerializeToString,
        response_deserializer=pokedex__service__pb2.GetPokemon_Response.FromString,
        )


class PokedexServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetPokemon(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PokedexServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetPokemon': grpc.unary_unary_rpc_method_handler(
          servicer.GetPokemon,
          request_deserializer=pokedex__service__pb2.GetPokemon_Request.FromString,
          response_serializer=pokedex__service__pb2.GetPokemon_Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'PokedexService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

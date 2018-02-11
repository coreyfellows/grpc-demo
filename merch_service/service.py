from .grpc_gen.merch_service_pb2_grpc import MerchServiceServicer
from .grpc_gen.merch_service_pb2 import GetShirts_Response, GetRelatedShirts_Response
from clients.pokedex_service import PokedexService

def start_up():
    pass
    
class MerchService(MerchServiceServicer):
    def GetShirts(self, request, context):
        ret = GetShirts_Response()
        for id_, json in SHIRTS.items():
            shirt = ret.shirts.add()
            shirt.id = id_
            shirt.name = json['name']
        return ret

    def GetRelatedShirts(self, request, context):
        ret = GetRelatedShirts_Response()
        pkmn_loader = PokedexService().GetPokemon(SHIRTS[request.id]['associated_pkmn'])

        pkmn = pkmn_loader.result().descriptions[0]
        for id_, json in SHIRTS.items():
            if json['associated_pkmn'] in pkmn.evolutions:
                shirt = ret.shirts.add()
                shirt.id = id_
                shirt.name = json['name']
        return ret


SHIRTS = {
    1: {
        'name': 'Charmander Shirt',
        'associated_pkmn': 4
    },
    2: {
        'name': 'Charizard Shirt',
        'associated_pkmn': 6
    },
    3: {
        'name': 'Charmeleon Shirt',
        'associated_pkmn': 5
    },
    4: {
        'name': 'Pikachu Shirt',
        'associated_pkmn': 25
    },
    5: {
        'name': 'Raichu Shirt',
        'associated_pkmn': 26
    }    
}

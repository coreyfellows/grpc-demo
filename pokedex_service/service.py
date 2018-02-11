from .grpc_gen.pokedex_service_pb2_grpc import PokedexServiceServicer
from .grpc_gen.pokedex_service_pb2 import GetPokemon_Response, PokemonDescription

def start_up():
    pass


    
class PokedexService(PokedexServiceServicer):
    def GetPokemon(self, request, context):
        ret = GetPokemon_Response()
        pokemon = POKEDEX
        if request.number:
            try:
                pokemon = [next(filter(lambda p: p['id'] == request.number, pokemon))]
            except:
                raise Exception(f"Pokemon {request.number} not found")

        for pkmn in pokemon:            
            description = ret.descriptions.add()
            description.number = pkmn['id']
            description.name = pkmn['name']
            for evo in pkmn.get('evolutions', []):
              description.evolutions.append(evo)
        return ret



POKEDEX = [
{
  "id": 1,
  "name": "Bulbasaur",
  "type": [ "grass", "poison" ],
},
{
  "id": 4,
  "name": "Charmander",
  "type": [ "fire" ],
  "evolutions": [5,6]
},
{
  "id": 5,
  "name": "Charmeleon",
  "type": [ "fire" ],
  "evolutions": [4,6]
},
{
  "id": 6,
  "name": "Charizard",
  "type": [ "fire" ],
  "evolutions": [4,5]
},
{
  "id": 26,
  "name": "Raichu",
  "type": [ "Electric"],
  "evolutions": [25]
},
{
  "id": 25,
  "name": "Pikachu",
  "type": [ "Electric" ],
  "evolutions": [26]
},
{
  "id": 15,
  "name": "Beedrill",
  "type": [ "bug", "poison" ],
},
{
  "id": 193,
  "name": "Yanma",
  "type": [ "bug", "flying" ],
},
{
  "id": 152,
  "name": "Chikorita",
  "type": [ "grass" ],
}
]
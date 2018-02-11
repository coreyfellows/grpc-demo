import discovery_service
import pokedex_service
import merch_service
import greeting_service
PORT = 8081

SERVICES, PORT = [discovery_service,pokedex_service, greeting_service], 8081
#SERVICES, PORT = [merch_service], 8082
DISCOVERY = {'Address': '127.0.0.1', 'Port': 8081}


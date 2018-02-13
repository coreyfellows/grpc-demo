from .grpc_gen.discovery_service_pb2_grpc import DiscoveryServiceServicer
from .grpc_gen.discovery_service_pb2 import Register_Response, GetServices_Response, ServiceDefinition

import json
import os


def start_up():
    services = {}
    save_registry(services)

def save_registry(services):
    with open(os.path.join('/','tmp','services.json'), 'w') as f:
        json.dump(services, f)
def get_registry():
    with open(os.path.join('/','tmp','services.json'), 'r') as f:
        return json.load(f)

class DiscoveryService(DiscoveryServiceServicer):
    def Register(self, request, context):
        services = get_registry()
        for name in request.service_name:
            if name not in services:
                services[name] = []
            services[name].append([request.address, request.port])
        save_registry(services)
        return Register_Response()

    def GetServices(self, request, context):
        response = GetServices_Response()

        services = get_registry()

        for service, servicers in services.items():
            definition = response.services.add()
            definition.name = service
            for address, port in servicers:
                definition.address.append(address)
                definition.port.append(port)
        return response

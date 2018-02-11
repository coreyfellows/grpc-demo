import grpc
import random
from collections import defaultdict

class BaseClient(object):
    
    def get_stub(self, service_name, method, request, stub_type):
        channel = None        
        if hasattr(self, "channel"):
            channel = self.channel

        if not channel and (self.ip_address and self.port):
            host = f'{self.ip_address}:{self.port}'
            self.channel = channel = grpc.insecure_channel(host)

        if channel:
            return stub_type(channel)
        return None

DISCOVERY = {'ip_address':'127.0.0.1', 'port':8081}

class DiscoveryClient(BaseClient):

    @classmethod
    def get_service(cls, service_name):
        from clients.discovery_service import DiscoveryService
        if not hasattr(cls, "service_registry") or not cls.service_registry[service_name]:
            response = DiscoveryService(**DISCOVERY).GetServices()
            cls.service_registry = registry = defaultdict(list)            
            for definition in response.result().services:
                registry[definition.name] = []
                for address, port in zip(definition.address, definition.port):
                    print (address, port)
                    registry[definition.name].append((address,port))
        return random.choice(cls.service_registry[service_name])

    def get_stub(self, service_name, method, request, stub_type):        
        stub = super().get_stub(service_name, method, request, stub_type)
        if stub:
            return stub
        
        addr, port = self.__class__.get_service(service_name)
        host = f'{addr}:{port}'
        self.channel = channel = grpc.insecure_channel(host)
        return stub_type(channel)
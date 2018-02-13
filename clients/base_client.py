import grpc
import random
from collections import defaultdict
import types

class BaseClient(object):

    def get_stub(self, service_name, method, request, stub_type):
        if self.mock:
            return self._mock_service

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

class FakeResponse(object):
    def __init__(self, response=None, exception=None):
        self._response = response
        self._exception = exception
    def result(self):
        if self._exception:
            raise self._exception
        return self._response
    def exception(self):
        return self._exception
    def done(self):
        return True

class FutureMeta(type):
    def __init__(cls, name, bases, dct):
        futures = []
        for name, ref in cls.__dict__.items():
            if not name.startswith('_') and hasattr(ref, "__call__"):
                futures.append(name)
        for name in futures:
            def _(request):
                try:
                    response = cls.__dict__[name](cls() ,request, None)
                    return FakeResponse(response=response)
                except Exception as e:
                    return FakeResponse(exception=e)


            cls.__dict__[name].future = lambda request: cls.__dict__[name](cls() ,request, None)
        super().__init__(name, bases, dct)

class MockService(object, metaclass=FutureMeta):
    pass


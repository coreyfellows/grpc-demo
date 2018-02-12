#WARNING: THIS IS GENERATED CODE GENERATED BY .\generate_proto.py.
#DO NOT TOUCH, RERUN THE GENERATOR.
from .discovery_service_pb2 import GetServices_Request, ServiceDefinition, GetServices_Response, Register_Request, Register_Response
from ..base_client import BaseClient
from .discovery_service_pb2_grpc import DiscoveryServiceStub


class DiscoveryService(BaseClient):
    def __init__(self,ip_address=None,port=None):
        self.ip_address, self.port = ip_address, port
    
    def Register(self,address=None,port=None,service_name=None):
        args = locals()
        del args["self"]
        request = Register_Request(**args)
        stub = self.get_stub("discovery_service", "Register", request, DiscoveryServiceStub)
        return stub.Register.future(request)
    
    def GetServices(self):
        args = locals()
        del args["self"]
        request = GetServices_Request(**args)
        stub = self.get_stub("discovery_service", "GetServices", request, DiscoveryServiceStub)
        return stub.GetServices.future(request)

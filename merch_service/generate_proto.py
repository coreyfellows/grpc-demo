from grpc_tools import protoc
import os
service_name = 'merch_service'
try:
    os.mkdir('grpc_gen')
except:
    pass
protoc.main(('', '-I.', '--python_out=./grpc_gen', '--grpc_python_out=./grpc_gen', f'./{service_name}.proto'))
try:
    os.mkdir(f'../clients/{service_name}')
except:
    pass
protoc.main(('', '-I.', f'--python_out=../clients/{service_name}', f'--grpc_python_out=../clients/{service_name}', f'./{service_name}.proto'))


for path in (os.path.join('grpc_gen') , os.path.join('..', 'clients', service_name)):
    filename = os.path.join(path, f'{service_name}_pb2_grpc.py')
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            if f'import {service_name}_pb2 as {service_name.replace("_", "__")}__pb2' in line:
                f.write(f'try:\n    {line}except:\n    from . {line}')
            else:
                f.write(line)


import grpc_gen.merch_service_pb2 as data_module
import grpc_gen.merch_service_pb2_grpc as rpc_module
from util import CodeGenerator


messages = {}
serializers = {}

app_name = "merch_service"

class dummy_channel(object):
    def unary_unary(self, name, request_serializer, response_deserializer):
        global serializers
        self.request = serializers[str(request_serializer)]
        return self.request


def generate(cg):

    for name, item in data_module.__dict__.items():
        if hasattr(item, 'DESCRIPTOR') and item.__class__.__name__ == 'GeneratedProtocolMessageType':
            messages[name] = [key for key in item.DESCRIPTOR.fields_by_name.keys()]
            serializers[str(item.SerializeToString)] = item


    #cg('from service_host.base_client import get_stub')
    cg(f'from .{app_name}_pb2 import {", ".join(messages.keys())}')
    cg("from ..base_client import DiscoveryClient")


    for name, item in rpc_module.__dict__.items():
        if not name.endswith('Stub'):
            continue

        stub = item(dummy_channel())
        cg(f'from .{app_name}_pb2_grpc import {name}')
        cg()
        cg()
        with cg.clss(name.replace('Stub', ''), base=('DiscoveryClient',)):
            with cg.method('__init__', ['ip_address', 'port'], ['None']*2):
                cg('self.ip_address, self.port = ip_address, port')
            for attr_name, attr in stub.__dict__.items():
                if not hasattr(attr, 'DESCRIPTOR'):
                    continue
                cg()
                #cg('@staticmethod')
                with cg.method(attr_name, messages[attr.DESCRIPTOR.name], ['None']*len(messages[attr.DESCRIPTOR.name])):
                    cg('args = locals()')
                    cg('del args["self"]')
                    cg(f'request = {attr.DESCRIPTOR.name}(**args)')
                    cg(f'stub = self.get_stub("{app_name}", "{attr_name}", request, {name})')
                    cg(f'return stub.{attr_name}.future(request)')


#cg = CodeGenerator(print)

with open(f'../clients/{app_name}/__init__.py', 'w') as f:
    cg = CodeGenerator(lambda l: f.write(f'{l}\n'))
    generate(cg)
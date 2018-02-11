from grpc_tools import protoc
import os
service_name = 'pokedex_service'

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

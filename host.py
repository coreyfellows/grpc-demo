import grpc
import argparse
from concurrent.futures import ThreadPoolExecutor
from config import SERVICES, DISCOVERY, PORT
from clients.discovery_service import DiscoveryService

if __name__ == "__main__":
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(f'[::]:{PORT}')
    services = []
    for service in SERVICES:
        service.initialize()
        service.add_to_server(server)
    
    server.start()
    discovery_client = DiscoveryService(DISCOVERY['Address'], DISCOVERY['Port'])
    names = [s.name for s in filter (lambda s: s.discoverable, SERVICES)]
    if names:
        response = discovery_client.Register('127.0.0.1', PORT, names)        
    
    input('\n')
    
    
    

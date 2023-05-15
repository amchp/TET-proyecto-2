from GRPC.generated.connection import Connection_pb2, Connection_pb2_grpc
from threading import Lock, Thread
from config import MAXIMUM


class ConnectionService(Connection_pb2_grpc.ConnectionServiceServicer):
    addresses = {}
    lock = Lock()

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def addAddresses(address, instance_id):
        with ConnectionService.lock:
            ConnectionService.addresses[address] = {
                "load" : 0,
                "instance_id": instance_id
            }
            
    @staticmethod
    def setLoad(address, load):
        with ConnectionService.lock:
            ConnectionService.addresses[address]["load"] = load
        
    @staticmethod
    def deleteAddresses(address):
        with ConnectionService.lock:
            if address not in address:
                return
            del ConnectionService.addresses[address]

    def onConnect(self, request, context):
        print(f'GRPC-CONNECTION-SERVICE: Connection request received from')
        print(f'GRPC-CONNECTION-SERVICE: Instance name: {request.instance_name}')
        print(f'GRPC-CONNECTION-SERVICE: IP address: {request.ip_address}')
        ConnectionService.addAddresses(request.ip_address, request.instance_name)
        print(ConnectionService.addresses, flush=True)
        return Connection_pb2.onConnectResponse(is_accepted=True)
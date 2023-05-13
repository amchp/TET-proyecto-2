from GRPC.generated.connection import Connection_pb2, Connection_pb2_grpc
from threading import Lock


class ConnectionService(Connection_pb2_grpc.ConnectionServiceServicer):
    addresses = {'0.0.0.0:8080': 0, '0.0.0.0:8081': 0}
    lock = Lock()

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def addAddresses(address):
        with ConnectionService.lock:
            ConnectionService.addresses[address] = 0
            
    @staticmethod
    def setLoad(address, load):
        with ConnectionService.lock:
            ConnectionService.addresses[address] = load
        
    @staticmethod
    def deleteAddresses(address):
        with ConnectionService.lock:
            del ConnectionService.addresses[address]

    def onConnect(self, request, context):
        print(f'GRPC-CONNECTION-SERVICE: Connection request received from')
        print(f'GRPC-CONNECTION-SERVICE: Instance name: {request.instance_name}')
        print(f'GRPC-CONNECTION-SERVICE: IP address: {request.ip_address}')
        ConnectionService.addAddresses(request.ip_address)
        print(ConnectionService.addresses, flush=True)
        return Connection_pb2.onConnectResponse(is_accepted=True)
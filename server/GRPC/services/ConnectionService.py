from GRPC.generated.connection import Connection_pb2, Connection_pb2_grpc


class ConnectionService(Connection_pb2_grpc.ConnectionServiceServicer):
    def __init__(self) -> None:
        super().__init__()


    def onConnect(self, request, context):
        print(f'GRPC-CONNECTION-SERVICE: Connection request received from')
        print(f'GRPC-CONNECTION-SERVICE: Instance name: {request.instance_name}')
        print(f'GRPC-CONNECTION-SERVICE: IP address: {request.ip_address}')
        
        return Connection_pb2.onConnectResponse(is_accepted=True)
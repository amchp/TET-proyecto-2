from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc


class HearbeatService(Heartbeat_pb2_grpc.HeartbeatServiceServicer):
    def __init__(self) -> None:
        super().__init__()


    def ping(self, request, context):
        print(f'GRPC-HEARTBEAT-SERVICE: Connection request received from')
        
        return Heartbeat_pb2.HeartbeatResponse(load=0.5)
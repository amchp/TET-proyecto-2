from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from threading import Lock


class HearbeatService(Heartbeat_pb2_grpc.HeartbeatServiceServicer):
    load = 0.1
    lock = Lock()
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def setLoad(load):
        with HearbeatService.lock:
            HearbeatService.load = load

    def ping(self, request, context):
        print(f'GRPC-HEARTBEAT-SERVICE: Connection request received from')
        
        return Heartbeat_pb2.HeartbeatResponse(load=HearbeatService.load)
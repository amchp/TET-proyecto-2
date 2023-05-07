import grpc
from google.protobuf.json_format import MessageToDict
from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from config import GRPC_TIMEOUT


def ping():
    a = "0.0.0.0:8080"
    
    with grpc.insecure_channel(a) as channel:
        stub = Heartbeat_pb2_grpc.HeartbeatServiceStub(channel)
        response = stub.ping(Heartbeat_pb2.Request(), timeout=GRPC_TIMEOUT)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        print(response_dict)
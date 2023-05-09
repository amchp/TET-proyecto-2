import grpc
from google.protobuf.json_format import MessageToDict
from GRPC.generated.connection import Connection_pb2, Connection_pb2_grpc
from config import GRPC_TIMEOUT


def connect():
    a = "0.0.0.0:8080"

    with grpc.insecure_channel(a) as channel:
        stub = Connection_pb2_grpc.ConnectionServiceStub(channel)
        response = stub.onConnect(
            Connection_pb2.onConnectRequest(
                instance_name="MACHINE", ip_address="1.1.1.1"
            ),
            timeout=GRPC_TIMEOUT,
        )
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        print(response_dict)

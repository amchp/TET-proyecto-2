import grpc
from google.protobuf.json_format import MessageToDict
from GRPC.generated.connection import Connection_pb2, Connection_pb2_grpc
from config import TARGET_CONNECTION, GRPC_TIMEOUT, PRIVATE_IP, INSTANCE_ID


def connect():

    with grpc.insecure_channel(TARGET_CONNECTION) as channel:
        stub = Connection_pb2_grpc.ConnectionServiceStub(channel)
        response = stub.onConnect(
            Connection_pb2.onConnectRequest(
                instance_name=INSTANCE_ID, ip_address=PRIVATE_IP
            ),
            timeout=GRPC_TIMEOUT,
        )
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        print(response_dict)

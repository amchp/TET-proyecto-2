# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import GRPC.generated.connection.Connection_pb2 as Connection__pb2


class ConnectionServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.onConnect = channel.unary_unary(
                '/ConnectionService/onConnect',
                request_serializer=Connection__pb2.onConnectRequest.SerializeToString,
                response_deserializer=Connection__pb2.onConnectResponse.FromString,
                )


class ConnectionServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def onConnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ConnectionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'onConnect': grpc.unary_unary_rpc_method_handler(
                    servicer.onConnect,
                    request_deserializer=Connection__pb2.onConnectRequest.FromString,
                    response_serializer=Connection__pb2.onConnectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ConnectionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ConnectionService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def onConnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ConnectionService/onConnect',
            Connection__pb2.onConnectRequest.SerializeToString,
            Connection__pb2.onConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

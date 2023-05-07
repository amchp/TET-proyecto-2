from concurrent import futures
import grpc
from .services.ConnectionService import ConnectionService
from GRPC.generated.connection import Connection_pb2_grpc
from config import GRPC_SERVER_PORT, SERVER_ADDRESS


def serveGRPC():    
    # Creating the server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Adding ConnectionService to the server
    Connection_pb2_grpc.add_ConnectionServiceServicer_to_server(ConnectionService(), server)

    # Starting the server
    print(f'GRPC server is listening on {SERVER_ADDRESS}:{str(GRPC_SERVER_PORT)}')
    server.add_insecure_port(SERVER_ADDRESS + ":" + str(GRPC_SERVER_PORT))
    server.start()
    server.wait_for_termination()
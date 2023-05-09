from GRPC.GRPCServer import serveGRPC
from GRPC.GRPCClient import connect
from threading import Thread


def runConnection():
    connect()

def runGRPCServer():
    serveGRPC()

if __name__ == '__main__':
    runConnection()
    # GRPCThread = Thread(target=runGRPCServer)
    # GRPCThread.start()
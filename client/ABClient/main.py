from GRPC.GRPCServer import serveGRPC
from GRPC.GRPCClient import connect
from threading import Thread
from API.api import runAPI


def runConnection():
    connect()

def runGRPCServer():
    serveGRPC()

if __name__ == '__main__':
    # runConnection()
    APIThread = Thread(target=runAPI)
    # GRPCThread = Thread(target=runGRPCServer)
    APIThread.start()
    # GRPCThread.start()
    
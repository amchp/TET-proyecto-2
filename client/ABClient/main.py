from GRPC.GRPCServer import serveGRPC
from GRPC.GRPCClient import connect
from threading import Thread
from API.api import runAPI


def runConnection():
    connect()

def runGRPCServer():
    serveGRPC()

if __name__ == '__main__':
    runConnection()
    GRPCThread = Thread(target=runGRPCServer)
    APIThread = Thread(target=runAPI)
    GRPCThread.start()
    APIThread.start()
    
    
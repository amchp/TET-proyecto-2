from time import sleep
from GRPC.GRPCServer import serveGRPC
from GRPC.GRPCClient import connect
from threading import Thread
from API.api import runAPI


def runConnection():
    connect()

def runGRPCServer():
    serveGRPC()

if __name__ == '__main__':
    GRPCThread = Thread(target=runGRPCServer)
    GRPCThread.start()
    sleep(3)
    runConnection()
    APIThread = Thread(target=runAPI)
    
    APIThread.start()
    
    
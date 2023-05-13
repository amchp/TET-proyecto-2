from GRPC.GRPCServer import serveGRPC
from threading import Thread
from GRPC.GRPCClient import continuouslyPing
from GRPC.API.api import runAPI

def startEC2():
    # Start desired EC2
    pass

def runGRPCServer():
    serveGRPC()

def runContinuouslyPing():
    continuouslyPing()

if __name__ == '__main__':
    # startEC2()
    # APIThread = Thread(target=runAPI)
    # GRPCThread = Thread(target=runGRPCServer)
    constantPing = Thread(target=runContinuouslyPing)
    # GRPCThread.start()
    constantPing.start()
    # APIThread.start()
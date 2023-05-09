from GRPC.GRPCServer import serveGRPC
from threading import Thread
from GRPC.GRPCClient import continuouslyPing

def startEC2():
    # Start desired EC2
    pass

def runGRPCServer():
    serveGRPC()

def runContinuouslyPing():
    continuouslyPing()

if __name__ == '__main__':
    # startEC2()
    GRPCThread = Thread(target=runGRPCServer)
    # constantPing = Thread(target=runContinuouslyPing)
    GRPCThread.start()
    # constantPing.start()
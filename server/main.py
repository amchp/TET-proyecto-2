from GRPC.GRPCServer import serveGRPC
from threading import Thread
from GRPC.GRPCClient import ping

def runGRPCServer():
    serveGRPC()


if __name__ == '__main__':
    #GRPCThread = Thread(target=runGRPCServer)
    #GRPCThread.start()
    ping()
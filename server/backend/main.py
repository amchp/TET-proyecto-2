from GRPC.GRPCServer import serveGRPC
from threading import Thread
from GRPC.GRPCClient import continuouslyPing
from GRPC.API.api import runAPI
from AWS.AWS import AWS_SERVICE
from config import DESIRED



def startEC2():
    AWS_SERVICE.create_ec2_instance(DESIRED)

def runGRPCServer():
    serveGRPC()

def runContinuouslyPing():
    continuouslyPing()

if __name__ == '__main__':
    APIThread = Thread(target=runAPI)
    APIThread.start()
    GRPCThread = Thread(target=runGRPCServer)
    constantPing = Thread(target=runContinuouslyPing)
    startEC2()
    GRPCThread.start()
    constantPing.start()
    
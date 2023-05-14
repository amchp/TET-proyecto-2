import grpc
from google.protobuf.json_format import MessageToDict
from multiprocessing.pool import ThreadPool
from time import time
from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from GRPC.services.ConnectionService import ConnectionService
from config import GRPC_TIMEOUT, DESIRED, MAXIMUM

startTime = time()

def sendPingToAddress(address):
    with grpc.insecure_channel(address) as channel:
        stub = Heartbeat_pb2_grpc.HeartbeatServiceStub(channel)
        response = stub.ping(Heartbeat_pb2.Request(), timeout=GRPC_TIMEOUT)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        load = response_dict['load']
        ConnectionService.setLoad(address, load)
        print(f'GRPC-HEARTBEAT-SERVICE: load received {address} {load}', flush=True)
        return load

def serverSwitch(address):
    # Create new AWS EC2
    ConnectionService.deleteAddresses(address)
    # print("Delete")

def ping(address):
    try:
        return sendPingToAddress(address)
    except:
        serverSwitch(address)
        
def autoScaling(meanLoad):
    global startTime
    if startTime is None:
        startTime = time()
    currentTime = time()
    # print(startTime, currentTime, flush=True)
    # Maybe it would be better 
    if currentTime < startTime + 300:
        return
    startTime = time()
    if meanLoad >= 60 and len(ConnectionService.addresses) < MAXIMUM:
        # New machine
        pass
        return
    if meanLoad < 60 and len(ConnectionService.addresses) > DESIRED:
        # Terminate machine
        pass
        return

def sendPingToAllAddress():
    addresses = ConnectionService.addresses.copy()
    with ThreadPool() as pool:
        result = pool.map_async(ping, addresses.keys())
        result.wait()
        meanLoad = sum(result.get())
    meanLoad /= len(addresses) if len(addresses) else 1
    print(f'Mean load {meanLoad}', flush=True)
    autoScaling(meanLoad)
    
def continuouslyPing():
    prevTime = 0
    curTime = 5
    while True:
        while curTime - prevTime < 5:
            curTime = time()
        prevTime = time()
        sendPingToAllAddress()
        curTime = time()
import grpc
from google.protobuf.json_format import MessageToDict
from threading import Thread
from time import time
from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from GRPC.services.ConnectionService import ConnectionService
from config import GRPC_TIMEOUT, DESIRED, MAXIMUM

meanLoad = 0
startTime = time()

def sendPingToAddress(address):
    with grpc.insecure_channel(address) as channel:
        stub = Heartbeat_pb2_grpc.HeartbeatServiceStub(channel)
        response = stub.ping(Heartbeat_pb2.Request(), timeout=GRPC_TIMEOUT)
        response_dict = MessageToDict(response, preserving_proto_field_name=True)
        load = response_dict['load']
        print(f'GRPC-HEARTBEAT-SERVICE: load received {address} {load}', flush=True)
        return load

def serverSwitch(i):
    # Create new AWS EC2
    # ConnectionService.deleteAddresses(i)
    print("Delete")

def ping(i, address):
    global meanLoad
    try:
        meanLoad += sendPingToAddress(address)
    except:
        serverSwitch(i)
        
def autoScaling():
    global meanLoad, startTime
    if startTime is None:
        startTime = time()
    currentTime = time()
    print(startTime, currentTime, flush=True)
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
    global meanLoad
    addresses = ConnectionService.addresses.copy()
    threads = []
    meanLoad = 0
    for i in range(len(addresses)):
        threads.append(Thread(target=ping, args=(i, addresses[i])))
        threads[i].start()
    for thread in threads:
        thread.join()
    meanLoad /= len(addresses) if len(addresses) else 1
    print(f'Mean load {meanLoad}', flush=True)
    autoScaling()
    
def continuouslyPing():
    while True:
        sendPingToAllAddress()
import grpc
from google.protobuf.json_format import MessageToDict
from multiprocessing.pool import ThreadPool
from threading import Thread
from time import time
from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from GRPC.services.ConnectionService import ConnectionService
from config import GRPC_TIMEOUT, DESIRED, MAXIMUM
from server.AWS.AWS import AWS_SERVICE

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

def terminate_instance(address):
    instance_id = AWS_SERVICE.get_instance_by_ip(address.partition(":"))
    AWS_SERVICE.terminate_instance(instance_id)

def serverSwitch(address):
    # Create new AWS EC2
    Thread(target=terminate_instance, args=[address]).start()
    ConnectionService.deleteAddresses(address)
    AWS_SERVICE.create_ec2_instance()
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
        Thread(target=AWS_SERVICE.create_ec2_instance).start()
        return
    if meanLoad < 60 and len(ConnectionService.addresses) > DESIRED:
        address = ConnectionService.addresses[-1]
        Thread(target=terminate_instance, args=[address]).start()
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
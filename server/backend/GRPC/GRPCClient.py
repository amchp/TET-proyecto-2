import grpc
from google.protobuf.json_format import MessageToDict
from multiprocessing.pool import ThreadPool
from threading import Thread
from time import time
from GRPC.generated.heartbeat import Heartbeat_pb2, Heartbeat_pb2_grpc
from GRPC.services.ConnectionService import ConnectionService
from config import GRPC_TIMEOUT, DESIRED, MAXIMUM
from AWS.AWS import AWS_SERVICE

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
    instance_id = ConnectionService.addresses[address]['instance_id']
    ConnectionService.deleteAddresses(address)
    AWS_SERVICE.terminate_instance(instance_id)

def serverSwitch(address):
    # Create new AWS EC2
    Thread(target=terminate_instance, args=[address]).start()
    AWS_SERVICE.create_ec2_instance()
    # print("Delete")

def ping(address):
    try:
        return sendPingToAddress(address)
    except:
        serverSwitch(address)
        return 0
    

        
def autoScaling(meanLoad):
    if ConnectionService.future_address > 0:
        return
    print("AutoScaling", flush=True)
    if meanLoad >= 0.6 and len(ConnectionService.addresses) < MAXIMUM:
        Thread(target=AWS_SERVICE.create_ec2_instance).start()
        return
    if meanLoad < 0.6 and len(ConnectionService.addresses) > DESIRED:
        address = list(ConnectionService.addresses.keys())[-1]
        Thread(target=terminate_instance, args=[address]).start()
        return
    if len(ConnectionService.addresses) < DESIRED:
        Thread(target=AWS_SERVICE.create_ec2_instance, args=[DESIRED - len(ConnectionService.addresses)]).start()
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
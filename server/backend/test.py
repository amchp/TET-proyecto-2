from GRPC.GRPCServer import serveGRPC
from threading import Thread
from GRPC.API.api import runAPI
from AWS.AWS import AWS_SERVICE

AWS_SERVICE.create_ec2_instance()
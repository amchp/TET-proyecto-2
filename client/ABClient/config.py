import os
BASE_DIR=os.getcwd()
TARGET_CONNECTION= ":8080"
SERVER_ADDRESS = os.getenv("PRIVATE_IP")
INSTANCE_ID = os.getenv("INSTANCE_ID")
API_PORT = 8000
GRPC_SERVER_PORT = 8080
GRPC_TIMEOUT = 5
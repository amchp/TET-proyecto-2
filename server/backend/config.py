import os
BASE_DIR=os.getcwd()
SERVER_ADDRESS = "0.0.0.0"
API_PORT=8000
GRPC_SERVER_PORT = 8080
GRPC_TIMEOUT = 5
MINIMUM=1
DESIRED=2
MAXIMUM=4

# AWS Params
AWS_ACCESS_KEY_ID = "asdasfasd" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AWS_SECRET_ACCES_KEY = "asdasd/asdasd/asdasd" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AWS_SESSION_TOKEN = "Un string muy largo con muchos /////// parentesis en medio asi" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AMI_ID = "ami-007855ac798b5175e" # Image of the instance to use, default is Ubuntu server 22.04 LTS 64-bit (x86)
LAUNCH_TEMPLATE_ID = "lt-02804de8dfbaa1bac"
REGION_NAME = "us-east-1"
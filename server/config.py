import os
BASE_DIR=os.getcwd()
SERVER_ADDRESS = "0.0.0.0"
GRPC_SERVER_PORT = 8080
GRPC_TIMEOUT = 5
MINIMUM=1
DESIRED=2
MAXIMUM=4

# AWS Params
AWS_ACCESS_KEY_ID = "ASDFGHH" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AWS_SECRET_ACCES_KEY = "ASD/SADASD/ASDASDASD/ASDA" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AWS_SESSION_TOKEN = "UnStringmuylargoconun/////////montondeparentesisenmedioasi" # IMPORTANTE, CAMBIAR ANTES DE SUBIR AL GITHUB
AMI_ID = "ami-007855ac798b5175e" # Image of the instance to use, default is Ubuntu server 22.04 LTS 64-bit (x86)
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "llaveEspadaWindows" # For connection via SSH to the instances
SECURITY_GROUP_ID = "sg-0e94f44b7461de06a"
REGION_NAME = "us-east-1"

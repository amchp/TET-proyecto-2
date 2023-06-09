from flask import Flask, abort
from flask_cors import CORS
from threading import Thread
from GRPC.services.ConnectionService import ConnectionService
from AWS.AWS import AWS_SERVICE
from config import SERVER_ADDRESS, API_PORT

app = Flask(__name__)
CORS(app)

@app.route("/servers/create/", methods=["POST"])
def createServer():    
    Thread(target=AWS_SERVICE.create_ec2_instance).start()
    return "", 201

@app.route("/servers/")
def servers():
    return ConnectionService.addresses

@app.route("/servers/<address>/", methods=["DELETE"])
def deleteServer(address):
    try:
        instance_id = ConnectionService.addresses[address]['instance_id']
        ConnectionService.deleteAddresses(address)
        AWS_SERVICE.terminate_instance(instance_id)
        return '', 204
    except:
        abort(404)

def runAPI():
    app.run(host=SERVER_ADDRESS, port=API_PORT)

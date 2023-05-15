from flask import Flask, abort
from threading import Thread
from GRPC.services.ConnectionService import ConnectionService
from AWS.AWS import AWS_SERVICE
from config import SERVER_ADDRESS, API_PORT, 

app = Flask(__name__)

@app.route("/servers/create/", methods=["POST"])
def createServer():
    Thread(target=AWS_SERVICE.create_ec2_instance).start()

@app.route("/servers/")
def servers():
    return ConnectionService.addresses

@app.route("/servers/<address>/", methods=["DELETE"])
def deleteServer(address):
    try:
        ConnectionService.deleteAddresses(address)
        return '', 204
    except:
        abort(404)

def runAPI():
    app.run(host=SERVER_ADDRESS, port=API_PORT)

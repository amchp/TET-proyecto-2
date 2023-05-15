from flask import Flask, abort
<<<<<<< HEAD
from flask_cors import CORS
=======
from threading import Thread
>>>>>>> 13e3d62741446ea7ee3a24f22d2e8a7695e116af
from GRPC.services.ConnectionService import ConnectionService
from AWS.AWS import AWS_SERVICE
from config import SERVER_ADDRESS, API_PORT

app = Flask(__name__)
CORS(app)

@app.route("/servers/create/", methods=["POST"])
def createServer():
    Thread(target=AWS_SERVICE.create_ec2_instance).start()

@app.route("/servers/")
def servers():
    return ConnectionService.addresses

@app.route("/servers/<address>/", methods=["DELETE"])
def deleteServer(address):
    print(f'API: Delete request received from {address}')
    return "", 204
    try:
        ConnectionService.deleteAddresses(address)
        return '', 204
    except:
        abort(404)

def runAPI():
    app.run(host=SERVER_ADDRESS, port=API_PORT)

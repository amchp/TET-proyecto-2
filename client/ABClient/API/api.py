from flask import Flask, request
from config import SERVER_ADDRESS, API_PORT
from GRPC.services.HeartbeatService import HearbeatService

app = Flask(__name__)

@app.route("/load/", methods=["POST"])
def setLoad():
    HearbeatService.setLoad(request.json['load'])
    return '', 200

def runAPI():
    app.run(host=SERVER_ADDRESS, port=API_PORT)

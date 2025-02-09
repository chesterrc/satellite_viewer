import datetime
from flask import Flask, request, jsonify
from sscws.sscws import SscWs 


app = Flask(__name__)
ssc = SscWs()


@app.get("/", method=["GET"])
def home():
    time = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    req = ssc.get_locations(["iss"], time)
    return jsonify(req)

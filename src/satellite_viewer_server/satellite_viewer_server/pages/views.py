import json
import attrs
from datetime import datetime, timedelta, timezone
from flask import jsonify, render_template
from satellite_viewer_server.conf import app, ssc 


@app.route("/", methods=["GET"])
def home():
    curr_time = datetime.now(timezone.utc)
    prev_time = (curr_time - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    time = [prev_time, curr_time.strftime("%Y-%m-%dT%H:%M:%SZ")]
    initial_poll = ssc.get_locations(["iss"], time)["Data"][0]["Coordinates"][0]
    app.logger.debug(f"time: {time}, inital_poll: {initial_poll} initial_poll data type: {type(initial_poll)}")

    req = {
            "X": initial_poll["X"].tolist(),
            "Y": initial_poll["Y"].tolist(),
            "Z": initial_poll["Y"].tolist()
            }

    return jsonify(req)

if __name__ == "__main__":
    app.run()

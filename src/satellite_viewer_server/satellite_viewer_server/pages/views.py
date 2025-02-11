import asyncio
from datetime import datetime, timedelta, timezone
from flask import jsonify, render_template
import satellite_viewer_server.pages.utils.data_parser
from satellite_viewer_server.conf import app, ssc 


@app.route("/", methods=["GET"])
async def home():
    curr_time = datetime.now(timezone.utc)
    prev_time = (curr_time - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    time = [prev_time, curr_time.strftime("%Y-%m-%dT%H:%M:%SZ")]

    try:
        initial_poll = ssc.get_locations(["iss"], time)["Data"]
    except Exception as e:
        raise Exception from e

    app.logger.debug(f"time: {time}, inital_poll: {initial_poll} initial_poll data type: {type(initial_poll)}")

    data =  await satellite_viewer_server.pages.utils.data_parser.parse_satellite_data(initial_poll)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

import asyncio
from datetime import datetime
from satellite_viewer_server.conf import app, ssc 


async def parse_satellite_data(data: list):
    parsed_data = {}

    for item in data:
        parsed_data[item["Id"]] = {
            "Coordinates": {
                "xyz": [(time.strftime("%Y-%m-%d %H:%M:%SZ"),
                       x_coord,
                       y_coord,
                       z_coord) for time, x_coord, y_coord, z_coord
                      in zip(item["Time"].tolist(),
                             item["Coordinates"][0]["X"],
                             item["Coordinates"][0]["Y"],
                             item["Coordinates"][0]["Z"]
                            )],
                "lat_lon": [(time.strftime("%Y-%m-%d %H:%M:%SZ"), lat, lon) for time, lat, lon
                            in zip(item["Time"].tolist(), 
                                   item["Coordinates"][0]["Latitude"],
                                   item["Coordinates"][0]["Longitude"])],
            }
        }

    return parsed_data
import json
import time

import websockets
import asyncio


async def handler(websocket):
    while True:
        # GPS = str(self.vehicle.gps_0)
        # battery = str(self.vehicle.battery)
        # altitude = str(self.vehicle.location.global_relative_frame.alt)
        # system = str(self.vehicle.system_status.state)
        # mode = str(self.vehicle.mode.name)
        # EKF = str(self.vehicle.ekf_ok)
        # location = str(self.vehicle.location.global_frame)
        # ip = str(self.ip)
        telemetry_dict = {
            "id": 3,  # ip ,
            "GPS": 'GPS',
            "Battery": 'battery',
            "Altitude": 'altitude',
            "System-status": 'system',
            "Vehicle-mode": 'mode',
            "EKF ok?": 'EKF',
            'location': 'location'
        }
        # async with websockets.connect('ws://192.168.73.223:8001') as ws:
        websocket.send(json.dumps(telemetry_dict))
        time.sleep(5)


async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


# run code here
if __name__ == "__main__":
    asyncio.run(main())

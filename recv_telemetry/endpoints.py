from flask import request
from auth.core import permission
from basehandler import api_response
from uploads.config import drone

telemetry = []


# {"id": 101, "GPS": 'GPSInfo:fix=3,num_sat=10', "Battery": "Battery:voltage=14.538,current=3.48,level=95", "EKFok": "Yes", "Altitude": 10, "Vehiclemode": 'GUIDED',
# 'location': [-0.205874,5.614818]},

# {"id": 102, "GPS": 'GPSInfo:fix=3,num_sat=10', "Battery": "Battery:voltage=12.538,current=3.48,level=99", "EKFok": "Yes", "Altitude": 15, "Vehiclemode": 'GUIDED',
# 'location': [-0.215874, 5.614818]}
def recv_telemetry():
    telemetry.clear()
    # tele = request.get_json()

    #if len(telemetry) != drone['number']:
    tele = request.get_json()
    telemetry.append(tele)
    #else:
    return 'ok'


def read_telemetry(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    return api_response({'result': telemetry})

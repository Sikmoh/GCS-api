from flask import request
from auth.core import permission
from basehandler import api_response
telemetry = [{"id": 101, "GPS": 10, "Battery": "15 volts", "EKFok": "Yes", "Altitude": 10, "Vehiclemode": 'GUIDED'},
             {"id": 102, "GPS": 12, "Battery": "16 volts", "EKFok": "Yes", "Altitude": 15, "Vehiclemode": 'GUIDED'},
             {"id": 103, "GPS": 10, "Battery": "14.5 volts", "EKFok": "Yes", "Altitude": 40, "Vehiclemode": 'GUIDED'},
             {"id": 104, "GPS": 5, "Battery": "13 volts", "EKFok": "Yes", "Altitude": 20, "Vehiclemode": 'GUIDED'}]


def recv_telemetry():
    telemetry.clear()
    tele = request.get_json()
    telemetry.append(tele)
    print(telemetry)
    return 'ok'


def read_telemetry(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    return api_response({'result': telemetry})

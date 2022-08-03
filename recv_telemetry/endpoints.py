from flask import request
from auth.core import permission
from basehandler import api_response
telemetry = []


def recv_telemetry(**kwargs):
    # print(telemetry)
    telemetry.clear()
    tele = request.get_json()
    telemetry.append(tele)
    print(telemetry)
    return 'ok'


def read_telemetry(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    return api_response({'result': telemetry})

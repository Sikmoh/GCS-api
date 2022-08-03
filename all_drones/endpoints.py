from auth.core import permission
from all_drones.data_access import *
from basehandler import api_response


def get_alldrones(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    data = [DroneDacc.all_drones(), DroneDacc.conn_dict()]

    return api_response({'result': data})

from select_drone.data_access import *
from auth.core import permission


def select_drone(**kwargs: dict):
    permission(kwargs['token_info'], access_role='basic')
    data = kwargs['body']
    SelectDacc.select(data['drone_id'], data['command'])
    return 'ok'

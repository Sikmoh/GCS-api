from connect.data_access import *
from auth.core import permission


def get_connection(**kwargs: dict):
    permission(kwargs['token_info'], access_role='basic')
    data = kwargs['body']
    # print(data)
    ConnectDacc.connect(data['connect'])
    return 'success'

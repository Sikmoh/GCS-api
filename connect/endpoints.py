from connect.data_access import *
from auth.core import permission
from uploads.config import drone


def make_connection(**kwargs: dict):
    permission(kwargs['token_info'], access_role='basic')
    ConnectDacc.connect(drone['number'])
    return 'success'

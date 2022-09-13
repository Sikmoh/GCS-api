from auth.core import permission
from command.data_access import *
from uploads.config import drone


def send_command(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    data = kwargs['body']
    CommandDacc.command(data['command'])
    return 'ok'


def take_off(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    data = kwargs['body']
    CommandDacc.command(data['command'] + drone['alt'])
    return 'ok'

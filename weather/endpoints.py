from weather.data_access import *
from basehandler import api_response
from auth.core import permission


def get_weather(**kwargs):
    permission(kwargs['token_info'], access_role='basic')
    data = WeatherDacc.forecasts(**kwargs)
    return api_response({'result': data})

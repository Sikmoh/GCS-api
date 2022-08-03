from weather.data_access import *
from basehandler import api_response


def get_weather(**kwargs):
    data = WeatherDacc.forecasts(**kwargs)
    return api_response({'result': data})

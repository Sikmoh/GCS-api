from weather.weather import *


class WeatherDacc:

    @staticmethod
    def forecast(**kwargs):
        forecast = Weather()
        forecast.request_data_sync('/data/2.5/weather', kwargs['lat'], kwargs['lon'], kwargs['units'],
                                   kwargs['appid'])
        return forecast.weather_data

    @staticmethod
    def forecasts(**kwargs):
        forecast = Weather()
        forecast.request_data_async('/data/2.5/weather', kwargs['lat'],kwargs['lon'], kwargs['units'],
                                    kwargs['appid'])
        return forecast.weather_data

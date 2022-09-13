from unittest import TestCase
from weather.weather import Weather


class TestFacts(TestCase):
    def test_request_data_sync(self):
        data = Weather()
        data.request_data_sync('/data/2.5/weather', '5.614818', '-0.205874', 'metric',
                               'be1a6f072ee128a15efcfe8ba62f6f14')
        assert data.weather_data['sys']['country'] == 'GH'

    def test_request_async(self):
        data = Weather()
        data.request_data_async('/data/2.5/weather', '5.614818', '-0.205874', 'metric',
                                'be1a6f072ee128a15efcfe8ba62f6f14')
        assert data.weather_data[0]['cod'] == 200

    def test_request_sync_len(self):
        data = Weather()
        data.request_data_async('/data/2.5/weather', '5.614818', '-0.205874', 'metric',
                                'be1a6f072ee128a15efcfe8ba62f6f14')
        print(data.weather_data)
        assert len(data.weather_data) == 1

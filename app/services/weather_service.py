import requests

from app.config.settings import WEATHER_API_KEY
from app.models.weather_model import WeatherData


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str):

        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "metric"
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

        weather = WeatherData(
            city=data["name"],
            country=data["sys"]["country"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            condition=data["weather"][0]["main"]
        )

        return weather
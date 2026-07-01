from pydantic import BaseModel


class WeatherData(BaseModel):
    city: str
    country: str
    temperature: float
    humidity: int
    wind_speed: float
    condition: str
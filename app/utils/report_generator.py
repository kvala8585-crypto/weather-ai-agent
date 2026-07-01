from app.models.weather_model import WeatherData


class ReportGenerator:

    def generate_report(self, weather: WeatherData) -> str:

        # Temperature Analysis
        if weather.temperature >= 35:
            temperature_status = "Very Hot"
        elif weather.temperature >= 25:
            temperature_status = "Warm"
        elif weather.temperature >= 15:
            temperature_status = "Pleasant"
        else:
            temperature_status = "Cold"

        # Humidity Analysis
        if weather.humidity >= 80:
            humidity_status = "High"
        elif weather.humidity >= 50:
            humidity_status = "Moderate"
        else:
            humidity_status = "Low"

        report = f"""
=========================================
            WEATHER REPORT
=========================================

City                : {weather.city}
Country             : {weather.country}

Temperature         : {weather.temperature} °C
Temperature Status  : {temperature_status}

Humidity            : {weather.humidity} %
Humidity Status     : {humidity_status}

Wind Speed          : {weather.wind_speed} m/s

Condition           : {weather.condition}

=========================================
"""

        return report
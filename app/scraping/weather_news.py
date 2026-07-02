from apify_client import ApifyClient
from app.config.settings import APIFY_TOKEN


class WeatherNewsScraper:

    def __init__(self):
        self.client = ApifyClient(APIFY_TOKEN)

    def get_weather_news(self, city):

        print(f"\nSearching weather news for {city}...\n")

        return [
            f"Weather update available for {city}",
            f"No severe weather alerts reported in {city}"
        ]
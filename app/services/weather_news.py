from apify_client import ApifyClient
from app.config.settings import APIFY_TOKEN


class WeatherNewsScraper:

    def __init__(self):
        self.client = ApifyClient(APIFY_TOKEN)

    def get_weather_news(self, city):

        try:
            run_input = {
                "q": f"{city} weather today",
                "maxResults": 5
            }

            run = self.client.actor("2Tg1MBeNzfI43XJGx").call(
                run_input=run_input
            )

            dataset_id = run["defaultDatasetId"]

            items = self.client.dataset(dataset_id).list_items().items

            news = []

            for item in items[:5]:

                title = (
                    item.get("title")
                    or item.get("heading")
                    or item.get("name")
                    or "Weather News"
                )

                news.append(title)

            return news

        except Exception as e:
            return [f"Apify Error: {e}"]
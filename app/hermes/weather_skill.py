from app.services.weather_service import WeatherService
from app.utils.report_generator import ReportGenerator
from app.scraping.weather_news import WeatherNewsScraper
from app.agents.ai_weather_agent import AIWeatherAgent
from app.prediction.prediction_engine import PredictionEngine
from app.trading.paper_trader import PaperTrader


class WeatherSkill:

    def __init__(self):

        self.weather_service = WeatherService()
        self.report_generator = ReportGenerator()
        self.news_scraper = WeatherNewsScraper()
        self.ai_agent = AIWeatherAgent()
        self.prediction_engine = PredictionEngine()
        self.paper_trader = PaperTrader()

    def execute(self, city: str):

        # Weather
        weather = self.weather_service.get_weather(city)

        # Report
        report = self.report_generator.generate_report(weather)

        # News
        news = self.news_scraper.get_weather_news(city)

        # AI Analysis
        analysis = self.ai_agent.analyze_weather(report)

        # Prediction
        prediction = self.prediction_engine.generate_prediction(
            analysis
        )

        # Paper Trade
        order = self.paper_trader.place_order(
            city,
            prediction,
            weather
        )

        return {
            "weather": weather,
            "report": report,
            "news": news,
            "analysis": analysis,
            "prediction": prediction,
            "order": order
        }
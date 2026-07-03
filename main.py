from app.services.weather_service import WeatherService
from app.utils.report_generator import ReportGenerator
from app.agents.ai_weather_agent import AIWeatherAgent
from app.prediction.prediction_engine import PredictionEngine
from app.trading.paper_trader import PaperTrader
from app.storage.trade_storage import TradeStorage
from app.analytics.statistics import Statistics
from app.scraping.weather_news import WeatherNewsScraper
from app.notifications.telegram_notifier import TelegramNotifier
from app.hermes.flow import HermesFlow


def main():

    service = WeatherService()
    report_generator = ReportGenerator()
    ai_agent = AIWeatherAgent()
    prediction_engine = PredictionEngine()
    paper_trader = PaperTrader()
    trade_storage = TradeStorage()
    statistics = Statistics()
    news_scraper = WeatherNewsScraper()
    telegram = TelegramNotifier() 
    hermes_flow = HermesFlow()

    print("=" * 60)
    print("           WEATHER AI AGENT")
    print("=" * 60)
    print("Type 'exit' to close the application.\n")

    while True:

        city = input("Enter City Name : ").strip()

        if city.lower() == "exit":
            print("\nThank you for using Weather AI Agent.")
            print("Goodbye!")
            break

        if city == "":
            print("Please enter a valid city name.\n")
            continue

        try:

            # Weather Data
            weather = service.get_weather(city)

            # Weather Report
            report = report_generator.generate_report(weather)
            # Hermes Analysis
            hermes_result = hermes_flow.run(city)

            # Weather News
            news = news_scraper.get_weather_news(city)

            # AI Analysis
            analysis = ai_agent.analyze_weather(report)

            # Prediction
            prediction = prediction_engine.generate_prediction(analysis)

            # Paper Trade
            order = paper_trader.place_order(
                city,
                prediction,
                weather
            )

            # Save Trade
            trade_storage.save_trade(order)

            # Telegram Alert
            telegram.send_trade_alert(order)

            print("\nTrade saved successfully.")
            print("-" * 50)

            # Statistics
            statistics.show_statistics()

            # Weather News
            print("\nWEATHER NEWS")
            print("-" * 50)

            if isinstance(news, list):
                if len(news) == 0:
                    print("No weather news found.")
                else:
                    for index, item in enumerate(news, start=1):
                        print(f"{index}. {item}")
            else:
                print(news)

            # AI Analysis
            print("\nAI ANALYSIS")
            print("-" * 50)
            print(analysis)

            # Prediction
            print("\nPREDICTION")
            print("-" * 50)
            print(f"Decision : {prediction['decision']}")
            print(f"Risk     : {prediction['risk']}")

            # Paper Trade
            print("\nPAPER TRADE")
            print("-" * 50)
            print(f"Date        : {order['date']}")
            print(f"City        : {order['city']}")
            print(f"Decision    : {order['decision']}")
            print(f"Risk        : {order['risk']}")
            print(f"Investment  : ${order['investment']}")
            print(f"Temperature : {order['temperature']} °C")
            print(f"Condition   : {order['condition']}")

            # Weather Report
            print("\nWEATHER REPORT")
            print("-" * 50)
            print(report)
            # Hermes Framework
            print("\nHERMES FRAMEWORK")
            print("-" * 50)

            hermes = hermes_result["hermes"]

            print(f"Framework     : {hermes['framework']}")
            print(f"Status        : {hermes['status']}")
            print(f"Summary       : {hermes['summary']}")

            if "report_length" in hermes:
                print(f"Report Length : {hermes['report_length']}")

            print("=" * 60)
            print(f"City        : {weather.city}")
            print(f"Country     : {weather.country}")
            print(f"Temperature : {weather.temperature} °C")
            print(f"Humidity    : {weather.humidity}%")
            print(f"Wind Speed  : {weather.wind_speed} m/s")
            print(f"Condition   : {weather.condition}")
            print("=" * 60)

        except Exception as e:

            print(f"\nError while processing '{city}'")
            print(e)
            print("-" * 60)


if __name__ == "__main__":
    main()
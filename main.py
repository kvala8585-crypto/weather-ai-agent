from app.services.weather_service import WeatherService
from app.utils.report_generator import ReportGenerator
from app.agents.ai_weather_agent import AIWeatherAgent
from app.prediction.prediction_engine import PredictionEngine
from app.trading.paper_trader import PaperTrader
from app.storage.trade_storage import TradeStorage
from app.analytics.statistics import Statistics


def main():

    service = WeatherService()
    report_generator = ReportGenerator()
    ai_agent = AIWeatherAgent()
    prediction_engine = PredictionEngine()
    paper_trader = PaperTrader()
    trade_storage = TradeStorage()
    statistics = Statistics()

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

            weather = service.get_weather(city)

            report = report_generator.generate_report(weather)

            analysis = ai_agent.analyze_weather(report)

            prediction = prediction_engine.generate_prediction(analysis)

            order = paper_trader.place_order(
                city,
                prediction,
                weather
            )

            # Save Trade History
            trade_storage.save_trade(order)

            print("\nTrade saved successfully.")
            print("-" * 50)

            # Show Statistics
            statistics.show_statistics()

            print("\nAI ANALYSIS")
            print("-" * 50)
            print(analysis)

            print("\nPREDICTION")
            print("-" * 50)
            print(f"Decision : {prediction['decision']}")
            print(f"Risk     : {prediction['risk']}")

            print("\nPAPER TRADE")
            print("-" * 50)
            print(f"Date        : {order['date']}")
            print(f"City        : {order['city']}")
            print(f"Decision    : {order['decision']}")
            print(f"Risk        : {order['risk']}")
            print(f"Investment  : ${order['investment']}")
            print(f"Temperature : {order['temperature']} °C")
            print(f"Condition   : {order['condition']}")

            print("\nWEATHER REPORT")
            print("-" * 50)
            print(report)

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
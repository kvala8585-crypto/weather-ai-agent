from app.hermes.hermes_agent import HermesWeatherAgent


def main():

    agent = HermesWeatherAgent()

    sample_report = """
    City : Ahmedabad
    Temperature : 31°C
    Humidity : 62%
    Condition : Clouds
    Wind Speed : 3.8 m/s
    """

    result = agent.analyze(sample_report)

    print("\n========== HERMES TEST ==========\n")

    for key, value in result.items():
        print(f"{key} : {value}")

    print("\n================================")


if __name__ == "__main__":
    main()
from app.hermes.weather_skill import WeatherSkill
from app.hermes.hermes_agent import HermesWeatherAgent


class HermesFlow:

    def __init__(self):

        self.skill = WeatherSkill()
        self.agent = HermesWeatherAgent()

    def run(self, city: str):

        result = self.skill.execute(city)

        hermes = self.agent.analyze(
            result["report"]
        )

        result["hermes"] = hermes

        return result
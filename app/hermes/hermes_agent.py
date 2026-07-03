import pkgutil


class HermesWeatherAgent:

    def __init__(self):
        self.framework = "Hermes Agent"

        installed_modules = [
            module.name.lower()
            for module in pkgutil.iter_modules()
        ]

        self.available = any(
            module.startswith("hermes")
            for module in installed_modules
        )

    def analyze(self, weather_report: str):

        if self.available:

            return {
                "framework": self.framework,
                "status": "Installed",
                "summary": "Hermes Agent framework detected successfully.",
                "report_length": len(weather_report)
            }

        return {
            "framework": self.framework,
            "status": "Not Installed",
            "summary": "Hermes Agent package was not found."
        }
from datetime import datetime


class PaperTrader:

    def place_order(self, city, prediction, weather):

        decision = prediction["decision"]
        risk = prediction["risk"]

        if risk == "LOW":
            investment = 100
        elif risk == "MEDIUM":
            investment = 50
        else:
            investment = 25

        order = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "city": city,
            "decision": decision,
            "risk": risk,
            "investment": investment,
            "temperature": weather.temperature,
            "condition": weather.condition
        }

        return order
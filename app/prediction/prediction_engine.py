class PredictionEngine:
    
    def generate_prediction(self, analysis: str):

        text = analysis.lower()

        # Risk
        if "high" in text:
            risk = "HIGH"

        elif "medium" in text:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        # Decision
        if (
            "good" in text
            or "clear" in text
            or "low risk" in text
            or "sunny" in text
        ):
            decision = "BUY"

        elif (
            "storm" in text
            or "heavy rain" in text
            or "high risk" in text
            or "danger" in text
        ):
            decision = "SELL"

        else:
            decision = "HOLD"

        return {
            "risk": risk,
            "decision": decision
        }
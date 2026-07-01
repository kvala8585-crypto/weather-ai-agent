import time

from openai import OpenAI
from app.config.settings import OPENROUTER_API_KEY


class AIWeatherAgent:

    def __init__(self):

        self.client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )

    def analyze_weather(self, report: str):

        prompt = f"""
You are an expert weather analyst.

Analyze this weather report.

{report}

Give:

1. Summary
2. Risk Level
3. Chance of Rain
4. Should someone consider trading on a weather prediction market?
"""

        retries = 3

        for attempt in range(retries):

            try:

                response = self.client.chat.completions.create(

                    model="qwen/qwen3-coder:free",

                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]

                )

                return response.choices[0].message.content

            except Exception as e:

                print(f"\nRetry {attempt + 1}/{retries}...")

                if attempt < retries - 1:
                    time.sleep(30)

                else:
                    return f"""
========================================
AI Analysis Unavailable
========================================

Reason:
{e}

OpenRouter Free Model is currently busy or rate-limited.

Please try again after a few minutes.
"""
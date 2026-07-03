import requests

from app.config.settings import (
    TELEGRAM_BOT_TOKEN,
    TELEGRAM_CHAT_ID
)


class TelegramNotifier:

    def __init__(self):

        self.token = TELEGRAM_BOT_TOKEN
        self.chat_id = TELEGRAM_CHAT_ID

    def send_trade_alert(self, order):

        if not self.token or not self.chat_id:
            print("Telegram credentials are missing.")
            return

        message = f"""
📢 WEATHER AI ALERT

🌍 City: {order['city']}

📈 Decision: {order['decision']}

⚠️ Risk: {order['risk']}

🌡 Temperature: {order['temperature']} °C

☁️ Condition: {order['condition']}

💰 Investment: ${order['investment']}
"""

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        payload = {
            "chat_id": self.chat_id,
            "text": message
        }

        try:

            response = requests.post(
                url,
                data=payload,
                timeout=10
            )

            if response.status_code == 200:
                print("\nTelegram alert sent successfully.")

            else:
                print("\nTelegram Error:")
                print(response.text)

        except Exception as e:
            print("\nTelegram Exception:")
            print(e)
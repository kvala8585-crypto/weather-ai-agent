import csv
import os


class TradeStorage:

    def __init__(self):

        self.filename = "trade_history.csv"

        if not os.path.exists(self.filename):

            with open(self.filename, "w", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Date",
                    "City",
                    "Decision",
                    "Risk",
                    "Investment",
                    "Temperature",
                    "Condition"
                ])

    def save_trade(self, order):

        with open(self.filename, "a", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow([
                order["date"],
                order["city"],
                order["decision"],
                order["risk"],
                order["investment"],
                order["temperature"],
                order["condition"]
            ])
import csv
import os


class Statistics:

    def show_statistics(self):

        filename = "trade_history.csv"

        if not os.path.exists(filename):
            print("No trade history found.")
            return

        total_trades = 0
        buy = 0
        sell = 0
        hold = 0

        low = 0
        medium = 0
        high = 0

        investment = 0

        with open(filename, "r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                total_trades += 1

                decision = row["Decision"]
                risk = row["Risk"]

                if decision == "BUY":
                    buy += 1

                elif decision == "SELL":
                    sell += 1

                else:
                    hold += 1

                if risk == "LOW":
                    low += 1

                elif risk == "MEDIUM":
                    medium += 1

                else:
                    high += 1

                investment += int(row["Investment"])

        print("\n")
        print("=" * 50)
        print("TRADING STATISTICS")
        print("=" * 50)

        print(f"Total Trades      : {total_trades}")
        print(f"BUY Trades        : {buy}")
        print(f"SELL Trades       : {sell}")
        print(f"HOLD Trades       : {hold}")

        print()

        print(f"LOW Risk          : {low}")
        print(f"MEDIUM Risk       : {medium}")
        print(f"HIGH Risk         : {high}")

        print()

        print(f"Total Investment  : ${investment}")

        print("=" * 50)
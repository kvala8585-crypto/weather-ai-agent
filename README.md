                                                     ## 🌦️ Weather AI Agent ##

A modular AI-powered Weather Agent built in **Python 3.11

	The application fetches live weather data, generates an AI weather analysis using OpenRouter, predicts trading decisions, simulates paper trading, stores trade history, scrapes weather news, sends Telegram alerts, and demonstrates Hermes Agent Framework integration.


#  Features

- 🌍 Live Weather Data (OpenWeather Map API)
- 🤖 AI Weather Analysis (OpenRouter LLM)
- 📰 Weather News Integration (Apify)
- 📩 Telegram Trade Alerts
- 🧠 Hermes Agent Framework Integration
- 📈 Prediction Engine
- 💵 Paper Trading Simulation
- 📊 Trading Statistics
- 📁 CSV Trade History Storage
- 📝 Weather Report Generator
- 🧱 Modular Project Structure
- ⚙️ Environment Variable Support
- 🛡️ Error Handling & Retry Logic
- 💻 Command Line Interface (CLI)

---

# 📁 Project Structure

```text
weather-ai-agent/

│
├── app/
│
├── agents/
│   ├── ai_weather_agent.py
│
├── analytics/
│   └── statistics.py
│
├── config/
│   └── settings.py
│
├── hermes/
│   ├── hermes_agent.py
│   ├── weather_skill.py
│   └── flow.py
│
├── models/
│   └── weather_model.py
│
├── notifications/
│   └── telegram_notifier.py
│
├── prediction/
│   └── prediction_engine.py
│
├── scraping/
│   └── weather_news.py
│
├── services/
│   └── weather_service.py
│
├── storage/
│   └── trade_storage.py
│
├── trading/
│   └── paper_trader.py
│
├── utils/
│   └── report_generator.py
│
├── data/
├── docs/
├── logs/
├── tests/
│
├── trade_history.csv
├── main.py
├── test_hermes.py
├── requirements.txt
├── README.md
└── .env.example
```


#  Technologies Used

- Python 3.11
- OpenWeatherMap API
- OpenRouter API
- OpenAI SDK
- Hermes Agent Framework
- Apify
- Telegram Bot API
- Requests
- Python Dotenv
- CSV Storage
- Logging

---

#  AI Model

Provider

OpenRouter

Model Used

```
qwen/qwen3-coder:free
```

Supported Models

- qwen/qwen3-coder:free
- meta-llama/llama-3.3-70b-instruct:free
- google/gemma-3-27b-it

---

#  Workflow

```text
User

↓

Enter City

↓

OpenWeatherMap API

↓

Weather Report

↓

Apify Weather News

↓

AI Weather Analysis

↓

Prediction Engine

↓

Paper Trading

↓

Telegram Notification

↓

CSV Storage

↓

Statistics

↓

Hermes Framework Analysis
```

---

# Hermes Agent Framework

The project demonstrates Hermes Agent integration.

Hermes performs an additional agent-level analysis after the weather report is generated.

It returns

- Framework Status
- Initialization Status
- Summary
- Report Length

Hermes components

- hermes_agent.py
- weather_skill.py
- flow.py

Test File

```
python test_hermes.py
```

---

# Weather News

Weather news is fetched using

- Apify Client
- Apify Token

News is displayed before AI Analysis.

---

# Telegram Notification

After every paper trade

The application automatically sends

- City
- Decision
- Risk
- Investment
- Temperature

to Telegram using a Telegram Bot.

---

# Paper Trading

Every prediction creates a simulated trade.

Decision

- BUY
- SELL
- HOLD

Risk

- LOW
- MEDIUM
- HIGH

Investment

- $100
- $50
- $25

---

#  Statistics

Displays

- Total Trades
- BUY Trades
- SELL Trades
- HOLD Trades
- LOW Risk
- MEDIUM Risk
- HIGH Risk
- Total Investment

---

# 📁 CSV Storage

All trades are automatically saved.

```
trade_history.csv
```

Columns

- Date
- City
- Decision
- Risk
- Investment
- Temperature
- Condition

---

#  Environment Variables

Create a

```
.env
```

file.

Example

```env
WEATHER_API_KEY=your_openweathermap_api_key

OPENROUTER_API_KEY=your_openrouter_api_key

APIFY_TOKEN=your_apify_api_token

TELEGRAM_BOT_TOKEN=your_telegram_bot_token

TELEGRAM_CHAT_ID=your_telegram_chat_id


---

#  Installation

Clone Repository

```bash
git clone <repository-url>
```

Go to Project

```bash
cd weather-ai-agent
```

Create Python 3.11 Virtual Environment

```bash
python -m venv venv311
```

Activate Virtual Environment

Windows

```bash
venv311\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run Application

```bash
python main.py
```

Hermes Test

```bash
python test_hermes.py
```

---

#  Sample Output

```text
==================================================
          WEATHER AI AGENT
==================================================

Enter City Name : Ahmedabad

Searching weather news...

WEATHER NEWS

1. Weather update available for Ahmedabad

AI ANALYSIS

Summary ...

PREDICTION

Decision : HOLD

Risk : LOW

PAPER TRADE

Investment : $100

Telegram Alert Sent

Trade saved successfully.

Statistics

Total Trades : 5

BUY : 1

SELL : 2

HOLD : 2

HERMES FRAMEWORK

Framework : Hermes Agent

Status : Installed

Summary : Hermes Agent framework detected successfully.
```

---

# Error Handling

The application handles

- Invalid City
- API Errors
- Network Failures
- Missing Environment Variables
- Telegram Errors
- OpenRouter Rate Limit
- Apify Errors
- Retry Logic

---

#  Future Improvements

- Real-Time Weather News
- Dashboard
- Database Storage
- Docker Support
- FastAPI API
- Web Interface
- Multi-City Monitoring
- Scheduled Weather Alerts

---

#  Author

**Kavi Vala**

AI Automation & Python Developer
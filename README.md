# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot for Binance Futures Testnet.

---

# Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Input validation
- Logging support
- Error handling
- Structured reusable code

---

# Project Structure

trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│
├── cli.py
├── requirements.txt
├── README.md
└── .env

---

# Setup Instructions

## Create Virtual Environment

Then Run
python -m venv venv
Activate Environment
Windows
.\venv\Scripts\Activate.ps1
Install Dependencies
pip install -r requirements.txt
Run MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Run LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
Logging

Logs are stored inside:

logs/trading_bot.log
Assumptions
Python 3 is installed
Internet connection is available
Binance Testnet API may require verification
Demo Mode

If API keys are unavailable, the application automatically runs in demo simulation mode.

Technologies Used
Python
python-binance
argparse
logging
dotenv

---

# Step 3 — Save File 

Press:

text id="u4m8cx"
Ctrl + S
# Example Output

text
========== ORDER REQUEST ==========
Symbol      : BTCUSDT
Side        : BUY
Order Type  : MARKET
Quantity    : 0.001
===================================

========== ORDER RESPONSE ==========
Order ID       : DEMO12345
Status         : SIMULATED
Executed Qty   : 0.001
Average Price  : Market Price
====================================

✅ Order placed successfully
# Note

Due to Binance Futures Testnet API verification restrictions, the project currently runs in demo simulation mode without live API credentials.
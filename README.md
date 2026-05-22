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

<img width="219" height="379" alt="Screenshot 2026-05-22 142740" src="https://github.com/user-attachments/assets/ca261f80-8a84-4614-8e20-f0f30dc62b25" />

---

# Setup Instructions

## Create Virtual Environment

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
<img width="377" height="403" alt="Screenshot 2026-05-22 142914" src="https://github.com/user-attachments/assets/f36a982b-2176-45be-b8fd-39fb63229136" />



# Note
Due to Binance Futures Testnet API verification restrictions, the project currently runs in demo simulation mode without live API credentials.

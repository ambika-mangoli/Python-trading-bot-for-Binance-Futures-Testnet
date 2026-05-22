import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")


class BinanceFuturesClient:

    def __init__(self):

        if not API_KEY or not API_SECRET:

            print("⚠ API keys not found. Running in demo mode.")

            self.client = None

        else:

            from binance.client import Client

            self.client = Client(API_KEY, API_SECRET)

            self.client.FUTURES_URL = (
                "https://testnet.binancefuture.com/fapi"
            )

    def get_client(self):

        return self.client
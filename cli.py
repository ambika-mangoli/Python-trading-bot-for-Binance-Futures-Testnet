import argparse

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager

from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from bot.logging_config import logger


def main():

    parser = argparse.ArgumentParser(
        description="Binance Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(args.side)

        order_type = validate_order_type(args.type)

        quantity = validate_quantity(args.quantity)

        price = validate_price(args.price, order_type)

        print("\n========== ORDER REQUEST ==========")

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if price:
            print(f"Price       : {price}")

        print("===================================\n")

        client = BinanceFuturesClient().get_client()

        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("========== ORDER RESPONSE ==========")

        print(f"Order ID       : {response.get('orderId')}")
        print(f"Status         : {response.get('status')}")
        print(f"Executed Qty   : {response.get('executedQty')}")
        print(f"Average Price  : {response.get('avgPrice')}")

        print("====================================")

        print("\n✅ Order placed successfully")

    except ValueError as e:

        logger.error(str(e))

        print(f"\n❌ Validation Error: {e}")

    except Exception as e:

        logger.error(str(e))

        print(f"\n❌ Failed to place order: {e}")


if __name__ == "__main__":
    main()
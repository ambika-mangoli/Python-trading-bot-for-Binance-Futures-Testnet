from bot.logging_config import logger


class OrderManager:

    def __init__(self, client):

        self.client = client

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        logger.info(
            f"Order Request => Symbol: {symbol}, "
            f"Side: {side}, Type: {order_type}, "
            f"Qty: {quantity}, Price: {price}"
        )

        if self.client is None:

            demo_response = {
                "orderId": "DEMO12345",
                "status": "SIMULATED",
                "executedQty": quantity,
                "avgPrice": price if price else "Market Price"
            }

            logger.info(f"Demo Response => {demo_response}")

            return demo_response

        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )

        logger.info(f"API Response => {response}")

        return response
VALID_SIDES = ["BUY", "SELL"]

VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_side(side):

    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError("Invalid side. Use BUY or SELL")

    return side


def validate_order_type(order_type):

    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError("Invalid order type")

    return order_type


def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price, order_type):

    if order_type == "LIMIT":

        if price is None:
            raise ValueError("Price required for LIMIT order")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

    return price
from config.settings import PRODUCT_KEY
from config.settings import QUANTITY_KEY
from config.settings import PRICE_KEY

def calculate_order_total(order, idx):
    product = order.get(PRODUCT_KEY)
    qty = order.get(QUANTITY_KEY)
    price = order.get(PRICE_KEY)

    if not product:
        raise ValueError(f"Missing product in order {idx}")
    if not isinstance(qty, int) or qty <= 0:
        raise ValueError(f"Invalid quantity for {product}")
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError(f"Invalid price for {product}")

    return product, qty * price

import json
from decimal import Decimal

from shop.products.models import Item


def get_selected_currency(request_body: bytes) -> str | None:
    """Read request body, return 'currency' value"""
    try:
        return json.loads(request_body).get("currency", None)
    except json.decoder.JSONDecodeError:
        return None


def convert_currency_symbol_to_stripe_type(symbol: str) -> str:
    """Convert currency symbol into stripe type currency"""

    match symbol:
        case Item.Currency.RUB:
            return "rub"
        case Item.Currency.USD:
            return "usd"
        case _:
            return "rub"


def convert_price_by_currency(
    symbol: str, item_price: Decimal, item_currency: str
) -> Decimal:
    """Convert price by given currency symbol, according to conversion_rates"""
    conversion_rate = 70
    if symbol == item_currency:
        return item_price
    elif symbol == Item.Currency.RUB:
        return item_price * conversion_rate
    elif symbol == Item.Currency.USD:
        return item_price / conversion_rate
    else:
        return item_price


def convert_price_to_cents(price: Decimal) -> int:
    return int(price * 100)

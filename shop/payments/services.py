import json
from decimal import Decimal

import stripe
from django.conf import settings

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
    expected_currency: str, item_price: Decimal, item_currency: str
) -> Decimal:
    """Compare expected_currency and item_currency, convert if not equal by conversion_rate"""
    conversion_rate = 70
    if expected_currency == item_currency:
        return item_price
    elif expected_currency == Item.Currency.RUB:
        return item_price * conversion_rate
    elif expected_currency == Item.Currency.USD:
        return item_price / conversion_rate
    else:
        return item_price


def convert_price_to_cents(price: Decimal) -> int:
    return int(price * 100)


def create_stripe_session(
    *,
    product_name: str,
    quantity: int = 1,
    currency: str,
    price_x100: int,
    success_url: str,
    cancel_url: str,
    methods: list[str] = ["card"],
) -> stripe.checkout.Session:
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=methods,
        line_items=[
            {
                "price_data": {
                    "currency": currency,
                    "product_data": {
                        "name": product_name,
                    },
                    "unit_amount": price_x100,
                },
                "quantity": quantity,
            }
        ],
        mode="payment",
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session

import json
from decimal import Decimal

import pytest

from shop.products.tests.factories import Item, ItemFactory

from ..services import (
    convert_currency_symbol_to_stripe_type,
    convert_price_by_currency,
    convert_price_to_cents,
    get_selected_currency,
)


def test_get_selected_currency():
    body = json.dumps({"currency": Item.Currency.RUB})
    result = get_selected_currency(body)
    assert result == Item.Currency.RUB


def test_get_selected_currency_blank():
    body = json.dumps({})
    result = get_selected_currency(body)
    assert not result


def test_convert_currency_symbol_to_stripe_type_rub():
    assert convert_currency_symbol_to_stripe_type(Item.Currency.RUB) == "rub"


def test_convert_currency_symbol_to_stripe_type_usd():
    assert convert_currency_symbol_to_stripe_type(Item.Currency.USD) == "usd"


def test_convert_currency_symbol_to_stripe_type_unknown():
    assert convert_currency_symbol_to_stripe_type("123") == "rub"


def test_convert_price_by_currency_rub():
    price = Decimal("1000.00")
    result = convert_price_by_currency(Item.Currency.RUB, price)
    assert result == price


def test_convert_price_by_currency_usd():
    price = Decimal("1000.00")
    result = convert_price_by_currency(Item.Currency.USD, price)
    assert result == price / 70


def test_convert_price_by_currency_unknown():
    price = Decimal("1000.00")
    result = convert_price_by_currency("123", price)
    assert result == price


@pytest.mark.django_db
def test_convert_price_to_cents():
    item = ItemFactory()
    assert int(item.price * 100) == convert_price_to_cents(item.price)

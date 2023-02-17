import pytest

from shop.products.tests.factories import Item, ItemFactory

from ..services import convert_currency_symbol_to_stripe_type, convert_price_to_cents


def test_convert_currency_symbol_to_stripe_type_rub():
    assert convert_currency_symbol_to_stripe_type(Item.Currency.RUB) == "rub"


def test_convert_currency_symbol_to_stripe_type_usd():
    assert convert_currency_symbol_to_stripe_type(Item.Currency.USD) == "usd"


def test_convert_currency_symbol_to_stripe_type_unknown():
    assert convert_currency_symbol_to_stripe_type("123") == "rub"


@pytest.mark.django_db
def test_convert_price_to_cents():
    item = ItemFactory()
    assert int(item.price * 100) == convert_price_to_cents(item.price)

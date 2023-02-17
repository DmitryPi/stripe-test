import random

from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal

from ..models import Item


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    name = Faker("sentence", nb_words=random.randrange(1, 4))
    description = Faker("text")
    price = FuzzyDecimal(50, 5000, precision=0)
    currency = Item.Currency.RUB

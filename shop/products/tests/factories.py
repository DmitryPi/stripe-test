from random import randrange

from factory import Faker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal

from ..models import Item


class ItemFactory(DjangoModelFactory):
    class Meta:
        model = Item

    name = Faker("sentence", nb_words=randrange(1, 4))
    description = Faker("text")
    price = FuzzyDecimal(50, 5000)

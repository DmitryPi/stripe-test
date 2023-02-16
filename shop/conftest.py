import pytest

from shop.products.tests.factories import Item, ItemFactory
from shop.users.models import User
from shop.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()


@pytest.fixture
def item(db) -> Item:
    return ItemFactory()

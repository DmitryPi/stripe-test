from shop.products.tests.factories import ItemFactory


def run():
    for _ in range(100):
        item = ItemFactory()
        print(f"Created: {item.name}")

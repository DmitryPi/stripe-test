from shop.products.models import Item


def run():
    items = Item.objects.all()
    for item in items:
        item.delete()

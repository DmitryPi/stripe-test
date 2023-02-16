from django.test import TestCase
from django.urls import reverse

from .factories import Item, ItemFactory


class ItemTests(TestCase):
    def setUp(self):
        self.item_data = {
            "name": "Футболка HyperX Xtreme",
            "description": "The best",
        }

    def test_create(self):
        batch_size = 5
        items = ItemFactory.create_batch(batch_size)
        self.assertEqual(len(items), batch_size)

    def test_read(self):
        item = ItemFactory(**self.item_data)
        read_item = Item.objects.get(id=item.id)
        self.assertEqual(read_item.name, self.item_data["name"])
        self.assertEqual(read_item.description, self.item_data["description"])

    def test_update(self):
        new_name = "Updated Test Item"
        item = ItemFactory(**self.item_data)
        item.name = new_name
        item.save()
        item.refresh_from_db()
        self.assertEqual(item.name, new_name)

    def test_delete(self):
        item = ItemFactory(**self.item_data)
        item.delete()
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=item.id)

    def test_str(self):
        item = ItemFactory(**self.item_data)
        str_repr = f"{item.pk} : {item.name} : {item.price}"
        self.assertEqual(str(item), str_repr)

    def test_get_absolute_url(self):
        item = ItemFactory(**self.item_data)
        url = reverse("products:item_detail", kwargs={"pk": item.pk})
        self.assertEqual(item.get_absolute_url(), url)

from django.test import TestCase
from django.urls import reverse

from .factories import ItemFactory


class ProductListViewTests(TestCase):
    def setUp(self):
        self.item_data = [
            {"name": "item 1", "price": 10},
            {"name": "item 2", "price": 20},
        ]
        ItemFactory(**self.item_data[0])
        ItemFactory(**self.item_data[1])

    def test_product_list_view(self):
        response = self.client.get(reverse("products:item_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item_data[0]["name"])
        self.assertContains(response, self.item_data[1]["name"])
        self.assertTemplateUsed(response, "products/list.html")


class ProductDetailViewTests(TestCase):
    def setUp(self):
        self.item_data = {"name": "item 1", "price": 10}
        self.item = ItemFactory(**self.item_data)

    def test_product_detail_view(self):
        response = self.client.get(
            reverse("products:item_detail", kwargs={"pk": self.item.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item_data["name"])
        self.assertTemplateUsed(response, "products/detail.html")

    def test_product_detail_view_invalid(self):
        response = self.client.get(reverse("products:item_detail", kwargs={"pk": 123}))
        self.assertEqual(response.status_code, 404)

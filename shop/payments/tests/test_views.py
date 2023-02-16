from django.test import TestCase
from django.urls import reverse

from shop.products.tests.factories import ItemFactory


class PaymentViewTests(TestCase):
    def setUp(self):
        self.item = ItemFactory()

    def test_payment_checkout(self):
        response = self.client.post(
            reverse("payments:checkout", kwargs={"pk": self.item.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_payment_success(self):
        response = self.client.get(reverse("payments:success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payments/success.html")

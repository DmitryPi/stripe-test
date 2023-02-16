from django.test import TestCase
from django.urls import reverse


class PaymentViewTests(TestCase):
    def setUp(self):
        pass

    def test_payment_checkout(self):
        response = self.client.post(reverse("payments:checkout"))
        self.assertEqual(response.status_code, 200)

    def test_payment_success(self):
        response = self.client.get(reverse("payments:success"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "payments/success.html")

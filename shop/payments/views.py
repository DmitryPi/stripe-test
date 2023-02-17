# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from shop.products.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class PaymentCheckoutView(View):
    def post(self, request, **kwargs):
        item = get_object_or_404(Item, **kwargs)
        selected_currency = "rub"
        success_url = request.build_absolute_uri(reverse("payments:success"))
        previous_url = request.META.get("HTTP_REFERER")
        # build session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": selected_currency,
                        "product_data": {
                            "name": item.name,
                        },
                        "unit_amount": item.price_in_cents,
                    },
                    "quantity": 1,
                }
            ],
            mode="payment",
            success_url=success_url,
            cancel_url=previous_url,
        )
        return JsonResponse({"id": session.id})


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"

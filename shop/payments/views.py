# Create your views here.
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def create_checkout_session(request):
    success_url = request.build_absolute_uri(reverse("payments:success"))
    previous_url = request.META.get("HTTP_REFERER")
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "inr",
                    "product_data": {
                        "name": "Intro to Django Course",
                    },
                    "unit_amount": 10000,
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

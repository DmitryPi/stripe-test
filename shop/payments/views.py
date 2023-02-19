from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from shop.products.models import Item

from .services import (
    convert_currency_symbol_to_stripe_type,
    convert_price_by_currency,
    convert_price_to_cents,
    create_stripe_checkout_session,
    get_selected_currency,
)


class PaymentCheckoutView(View):
    def post(self, request, **kwargs):
        currency = get_selected_currency(request.body)
        item = get_object_or_404(Item, **kwargs)
        item_price = convert_price_by_currency(currency, item.price, item.currency)
        item_price_in_cents = convert_price_to_cents(item_price)
        item_currency = convert_currency_symbol_to_stripe_type(currency)
        # build urls
        success_url = request.build_absolute_uri(reverse("payments:success"))
        previous_url = request.META.get("HTTP_REFERER")
        # create session
        session = create_stripe_checkout_session(
            product_name=item.name,
            currency=item_currency,
            price_x100=item_price_in_cents,
            success_url=success_url,
            cancel_url=previous_url,
        )
        return JsonResponse({"id": session.id})


class PaymentSuccessView(TemplateView):
    template_name = "payments/success.html"

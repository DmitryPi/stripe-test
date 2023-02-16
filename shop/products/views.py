import stripe
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY


class PaymentSuccessView(TemplateView):
    template_name = "products/payment_success.html"


class ItemListView(ListView):
    template_name = "products/list.html"
    model = Item


class ItemDetailView(DetailView):
    template_name = "products/detail.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["STRIPE_PUBLIC_KEY"] = STRIPE_PUBLIC_KEY
        return context

    def post(self, request, *args, **kwargs):
        """
        4242 4242 4242 4242
        112025
        000
        """
        item = self.get_object()

        # Get the credit card details submitted by the form
        token = request.POST["stripeToken"]
        email = request.POST["stripeEmail"]

        # Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=int(item.converted_form_price),
                currency="usd",
                source=token,
                description=f"Charge for {email}",
            )
            print(charge)
        except stripe.error.CardError as e:
            # The card has been declined
            print(e)

        # Redirect to the success page
        return HttpResponseRedirect(reverse("products:payment_success"))

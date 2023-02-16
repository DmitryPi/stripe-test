import stripe
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY
STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY


class ItemListView(ListView):
    template_name = "products/list.html"
    model = Item


class ItemDetailView(DetailView):
    template_name = "products/detail.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stripe_public_key"] = STRIPE_PUBLIC_KEY
        return context

    def post(self, request, *args, **kwargs):
        item = self.get_object()
        amount = item.price

        # Get the credit card details submitted by the form
        token = request.POST["stripeToken"]
        email = request.POST["stripeEmail"]

        # Create a charge: this will charge the user's card
        try:
            charge = stripe.Charge.create(
                amount=int(amount * 100),
                currency="usd",
                source=token,
                description=f"Charge for {email}",
            )
            print(charge)
        except stripe.error.CardError as e:
            # The card has been declined
            print(e)

        # Redirect to the success page
        return HttpResponseRedirect(reverse("payment_success"))

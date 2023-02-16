from django.conf import settings
from django.views.generic import DetailView, ListView

from .models import Item

STRIPE_PUBLIC_KEY = settings.STRIPE_PUBLIC_KEY


class ItemDetailView(DetailView):
    template_name = "products/detail.html"
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["STRIPE_PUBLIC_KEY"] = str(STRIPE_PUBLIC_KEY)
        return context


class ItemListView(ListView):
    template_name = "products/list.html"
    model = Item

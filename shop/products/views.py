from django.views.generic import DetailView, ListView

from .models import Item


class ItemListView(ListView):
    template_name = "products/list.html"
    model = Item


class ItemDetailView(DetailView):
    template_name = "products/detail.html"
    model = Item

from django.urls import path

from .apps import ProductsConfig
from .views import ItemDetailView, ItemListView

app_name = ProductsConfig.verbose_name

urlpatterns = [
    path("", ItemListView.as_view(), name="item_list"),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
]

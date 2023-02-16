from django.urls import path

from .apps import PaymentsConfig
from .views import PaymentCheckoutView, PaymentSuccessView

app_name = PaymentsConfig.verbose_name


urlpatterns = [
    path("buy/<int:pk>", PaymentCheckoutView.as_view(), name="checkout"),
    path("payment-success/", PaymentSuccessView.as_view(), name="success"),
]

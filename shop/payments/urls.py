from django.urls import path

from .apps import PaymentsConfig
from .views import PaymentSuccessView, create_checkout_session

app_name = PaymentsConfig.verbose_name


urlpatterns = [
    path("payment-checkout/", create_checkout_session, name="checkout"),
    path("payment-success/", PaymentSuccessView.as_view(), name="success"),
]

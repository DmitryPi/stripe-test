from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    # choices
    class Currency(models.TextChoices):
        RUB = "₽", _("RUB")
        USD = "$", _("USD")

    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(_("Price"), max_digits=11, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(
        max_length=3, choices=Currency.choices, default=Currency.RUB
    )

    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.pk} : {self.name} : {self.price}"

    def get_absolute_url(self):
        return reverse("products:item_detail", kwargs={"pk": self.pk})

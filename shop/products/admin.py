from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    readonly_fields = [
        "id",
        "updated_at",
        "created_at",
    ]
    list_display = [
        "__str__",
        "updated_at",
        "created_at",
    ]

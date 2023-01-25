from django.contrib import admin
from .models import Discount


class DiscountAdmin(admin.ModelAdmin):
    list_display = ["partner_name", "partner_offer"]

# Register your models here.
admin.site.register(Discount,DiscountAdmin)
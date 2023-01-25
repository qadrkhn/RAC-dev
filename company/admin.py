from django.contrib import admin
from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["partner_name", "website_url"]
    list_display_links = ["partner_name",]

# Register your models here.
admin.site.register(Company,CompanyAdmin)
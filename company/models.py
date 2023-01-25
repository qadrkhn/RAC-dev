from django.db import models

# Create your models here.
class Company(models.Model):
    partner_name = models.CharField(max_length=50)
    website_url = models.CharField(max_length=100)
    checkout_url = models.CharField(max_length=100)


    def __str__(self):
        return self.partner_name
from django.db import models
from company.models import Company
# Create your models here.
class Discount(models.Model):
    partner_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    partner_offer = models.CharField(max_length=150,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.partner_offer}"
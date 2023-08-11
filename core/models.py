from django.db import models
from authapp.models import CustomerPurchase
from django.utils import timezone



class Payment(models.Model):
    customerPurchase = models.ForeignKey(CustomerPurchase, on_delete=models.CASCADE, related_name="payments")
    date = models.DateField("To'lov Sanasi", default=timezone.now)
    amount = models.FloatField("Summa")
    createdAt = models.DateTimeField(auto_now_add=True)
    


class FinancialStatus(models.Model):
    customerPurchase = models.ForeignKey(CustomerPurchase, on_delete=models.CASCADE, related_name="financies")
    amount = models.FloatField("Summa")

    createdAt = models.DateTimeField(auto_now_add=True)


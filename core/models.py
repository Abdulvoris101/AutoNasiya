from django.db import models
from authapp.models import Customer
from django.utils import timezone


class CustomerPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    productName = models.CharField("Maxsulot nomi", max_length=255)
    costProduct = models.FloatField("Maxsulot tan narxi")
    startingFee = models.FloatField("Boshlang'ich to'lov")
    taxRate = models.FloatField("Soliq foizi")
    paymentDay = models.IntegerField("To'lov kuni", default=15)
    monthlyPaymentAmount = models.FloatField("Oylik tolov", null=True, blank=True)
    totalPrice = models.FloatField("Ummumiy summa", null=True, blank=True)

    duration = models.IntegerField(null=True, blank=True)
    startedAt = models.DateTimeField("Boshlanish sanasi", default=timezone.now)
    finishedAt = models.DateTimeField("Tugash sanasi")

    def __str__(self):
        return f"{self.customer.checkId} - {self.productName}"

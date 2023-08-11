from django.db import models
import shortuuid
from django.utils import timezone



class Customer(models.Model):
    checkId = models.CharField("Check Id", max_length=25, default=shortuuid.uuid)
    firstName = models.CharField("Ism", max_length=255)
    phoneNumber = models.CharField("Tel.raqam", max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phoneNumber} - {self.purchases.first().productName}"


    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"


class CustomerPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="purchases")
    productName = models.CharField("Maxsulot nomi", max_length=255)
    costProduct = models.FloatField("Maxsulot tan narxi")
    startingFee = models.FloatField("Boshlang'ich to'lov", default=0.0)
    taxRate = models.FloatField("Soliq foizi")
    paymentDay = models.IntegerField("To'lov kuni", default=15)
    amountOfMonth = models.FloatField("Oylik tolov", null=True, blank=True)
    totalPrice = models.FloatField("Ummumiy summa", null=True, blank=True)

    duration = models.IntegerField(null=True, blank=True)
    startedAt = models.DateTimeField("Boshlanish sanasi", default=timezone.now)
    finishedAt = models.DateTimeField("Tugash sanasi")


    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"


    def __str__(self):
        return f"{self.customer.checkId}, {self.productName}"

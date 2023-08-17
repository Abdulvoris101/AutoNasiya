from django.db import models
import shortuuid
from django.utils import timezone



class Customer(models.Model):
    checkId = models.CharField("Check Id", max_length=25, default=shortuuid.uuid, unique=True)
    firstName = models.CharField("Ism", max_length=255)
    phoneNumber = models.CharField("Tel.raqam", max_length=255, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.phoneNumber}"

    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"

STATUS_CHOISES = (
    ("OPEN", "Ochiq"),
    ("CLOSE", "Yopiq"),
)

class ProductPurchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="purchases")
    productName = models.CharField("Maxsulot nomi", max_length=255)
    costProduct = models.FloatField("Maxsulot tan narxi")
    startingFee = models.IntegerField("Boshlang'ich to'lov", default=0.0)
    taxRate = models.IntegerField("Soliq foizi", default=0)
    amountOfMonth = models.FloatField("Oylik tolov", null=True, blank=True)
    totalPrice = models.FloatField("Ummumiy summa", null=True, blank=True)

    nextPaymentAmount = models.FloatField("Keyingi to'lov summasi", null=True, blank=True)
    duration = models.IntegerField("Davomiyligi")
    status = models.CharField("Xisob", choices=STATUS_CHOISES, max_length=5, default="OPEN")
    startedAt = models.DateTimeField("Boshlanish sanasi", default=timezone.now)
    finishedAt = models.DateTimeField("Tugash sanasi",  null=True, blank=True)


    class Meta:
        verbose_name = "Maxsulot"
        verbose_name_plural = "Maxsulotlar"

    def __str__(self):
        return f"{self.customer.phoneNumber}, {self.productName}"

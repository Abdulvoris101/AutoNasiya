from django.db import models
import shortuuid


class Customer(models.Model):
    checkId = models.CharField("Check Id", max_length=25, default=shortuuid.uuid)
    firstName = models.CharField("Ism", max_length=255)
    phoneNumber = models.CharField("Tel.raqam", max_length=255, unique=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstName}-{self.phoneNumber}"
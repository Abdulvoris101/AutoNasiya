from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
import shortuuid


class Customer(AbstractBaseUser, PermissionsMixin):
    checkId = models.CharField("Check Id", max_length=25, default=shortuuid.uuid)
    firstName = models.CharField("Ism", max_length=255)
    phoneNumber = models.CharField("Tel.raqam", max_length=255)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "checkId"
    REQUIRED_FIELDS = ["firstName", "phoneNumber"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.firstName}-{self.phoneNumber}"
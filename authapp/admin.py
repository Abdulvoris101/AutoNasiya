from django.contrib import admin
from .models import Customer, CustomerPurchase


class CustomerPurchaseInline(admin.TabularInline):
    model = CustomerPurchase
    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration")
    extra = 1


@admin.register(CustomerPurchase)
class CustomerAdmin(admin.ModelAdmin):
    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration")
    list_display = ("customer", "productName", "amountOfMonth", "totalPrice", "duration")


@admin.register(Customer)
class Customer(admin.ModelAdmin):
    inlines = [CustomerPurchaseInline]
    list_display = ("firstName", "phoneNumber", "checkId")
    search_fields = ("phoneNumber", "checkId", "firstName")
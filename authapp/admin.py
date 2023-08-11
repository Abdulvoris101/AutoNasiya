from django.contrib import admin
from .models import Customer, CustomerPurchase
from core.models import Payment

class CustomerPurchaseInline(admin.TabularInline):
    model = CustomerPurchase
    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration")
    extra = 1


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 1


@admin.register(CustomerPurchase)
class CustomerPurchaseAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

    def get_customer_checkid(self, obj):
        return obj.customer.checkId

    get_customer_checkid.short_description = "Customer Check ID"

    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration")
    list_display = ("customer",  "productName", "get_customer_checkid", "amountOfMonth", "totalPrice", "duration")
    search_fields = ("productName", "customer__checkId")
    list_filter = ("customer", )



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerPurchaseInline]
    list_display = ("firstName", "phoneNumber", "checkId")
    search_fields = ("phoneNumber", "checkId", "firstName")
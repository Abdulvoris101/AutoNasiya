from django.contrib import admin
from .models import Customer, ProductPurchase
from core.models import Payment


class ProductPurchaseInline(admin.TabularInline):
    model = ProductPurchase
    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration")
    extra = 1


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0



@admin.register(ProductPurchase)
class ProductPurchaseAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

    def get_customer_checkid(self, obj):
        return obj.customer.checkId

    get_customer_checkid.short_description = "Customer Check ID"

    readonly_fields = ("id", "totalPrice", "amountOfMonth", "duration", "nextPaymentAmount")
    list_display = ("customer",  "productName", "get_customer_checkid", "paymentDay", "nextPaymentAmount", "totalPrice", "duration")
    search_fields = ("productName", "customer__checkId")
    list_filter = ("customer", )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [ProductPurchaseInline]
    list_display = ("firstName", "phoneNumber", "checkId")
    search_fields = ("phoneNumber", "checkId", "firstName")
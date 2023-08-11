from django.db.models.signals import post_save, pre_delete
from authapp.models import Customer, CustomerPurchase
from django.dispatch import receiver

@receiver(post_save, sender=CustomerPurchase)
def auto_calculate(sender, instance, created, **kwargs):
    if created:
        instance.totalPrice = (instance.taxRate / 100) * instance.costProduct + instance.costProduct

        instance.save()

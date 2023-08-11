from django.db.models.signals import post_save
from authapp.models import ProductPurchase
from django.dispatch import receiver
from core.models import FinancialStatus
from .utils import CalculateAutoFields


@receiver(post_save, sender=ProductPurchase)
def auto_calculate(sender, instance, created, **kwargs):

    if created:
        FinancialStatus.objects.create(productPurchase=instance, amount=0.0)


    if not kwargs.get('raw', False):
        autoFields = CalculateAutoFields(instance=instance)

        instance.totalPrice = autoFields.totalPrice
        instance.duration = autoFields.duration
        instance.amountOfMonth = autoFields.amountOfMonth
        instance.nextPaymentAmount = autoFields.nextPaymentAmount

        post_save.disconnect(auto_calculate, sender=ProductPurchase)
        instance.save()

        post_save.connect(auto_calculate, sender=ProductPurchase)

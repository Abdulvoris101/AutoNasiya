from django.db.models.signals import post_save, pre_delete
from authapp.models import CustomerPurchase
from django.dispatch import receiver
from dateutil.relativedelta import relativedelta

@receiver(post_save, sender=CustomerPurchase)
def auto_calculate(sender, instance, created, **kwargs):
    if created:
        instance.costProduct = instance.costProduct - instance.startingFee
        instance.totalPrice = (instance.taxRate / 100) * instance.costProduct + instance.costProduct
        duration = relativedelta(instance.finishedAt, instance.startedAt)
        instance.duration = duration.months + 12 * duration.years
        instance.amountOfMonth = instance.totalPrice / instance.duration
        instance.save()

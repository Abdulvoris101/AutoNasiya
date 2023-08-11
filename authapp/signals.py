from django.db.models.signals import post_save, pre_delete
from authapp.models import ProductPurchase
from django.dispatch import receiver

@receiver(post_save, sender=ProductPurchase)
def auto_calculate(sender, instance, **kwargs):

    if not kwargs.get('raw', False):
        post_save.disconnect(auto_calculate, sender=ProductPurchase)
        instance.save()
        post_save.connect(auto_calculate, sender=ProductPurchase)

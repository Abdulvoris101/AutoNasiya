# Generated by Django 4.2.4 on 2023-08-11 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_payment_customer_payment_customerpurchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financialstatus',
            old_name='customerPurchase',
            new_name='productPurchase',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='customerPurchase',
            new_name='productPurchase',
        ),
    ]

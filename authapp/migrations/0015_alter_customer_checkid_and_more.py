# Generated by Django 4.2.4 on 2023-08-11 17:13

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_remove_productpurchase_paymentday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkId',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=25, verbose_name='Check Id'),
        ),
        migrations.AlterField(
            model_name='productpurchase',
            name='duration',
            field=models.FloatField(blank=True, null=True, verbose_name='Davomiyligi'),
        ),
    ]

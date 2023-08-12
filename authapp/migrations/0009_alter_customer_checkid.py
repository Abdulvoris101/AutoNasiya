# Generated by Django 4.2.4 on 2023-08-11 12:53

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_alter_customer_checkid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkId',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=25, verbose_name='Check Id'),
        ),
    ]

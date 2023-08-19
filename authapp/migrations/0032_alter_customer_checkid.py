# Generated by Django 4.2.4 on 2023-08-19 10:36

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0031_customer_showedpassword_alter_customer_checkid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='checkId',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=25, unique=True, verbose_name='Check Id'),
        ),
    ]
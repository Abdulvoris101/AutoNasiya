# Generated by Django 4.2.4 on 2023-08-10 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerPurchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=255, verbose_name='Maxsulot nomi')),
                ('costProduct', models.FloatField(verbose_name='Maxsulot tan narxi')),
                ('startingFee', models.FloatField(verbose_name="Boshlang'ich to'lov")),
                ('taxRate', models.FloatField(verbose_name='Soliq foizi')),
                ('paymentDay', models.IntegerField(default=15, verbose_name="To'lov kuni")),
                ('monthlyPaymentAmount', models.FloatField(blank=True, null=True, verbose_name='Oylik tolov')),
                ('totalPrice', models.FloatField(blank=True, null=True, verbose_name='Ummumiy summa')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('startedAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Boshlanish sanasi')),
                ('finishedAt', models.DateTimeField(verbose_name='Tugash sanasi')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

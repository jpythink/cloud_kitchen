# Generated by Django 4.1.2 on 2022-11-10 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_transaction_amount_transaction_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='order_id',
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_remove_transaction_checksum'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
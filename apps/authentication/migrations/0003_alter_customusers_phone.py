# Generated by Django 4.1.2 on 2022-10-09 07:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_customusers_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='IN'),
        ),
    ]

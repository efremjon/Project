# Generated by Django 3.2.9 on 2022-05-14 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0054_auto_20220514_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_amount_in_store',
            name='product',
        ),
    ]

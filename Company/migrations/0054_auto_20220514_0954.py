# Generated by Django 3.2.9 on 2022-05-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0053_auto_20220514_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_amount_in_store',
            name='Name',
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='product',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-14 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0055_remove_product_amount_in_store_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Castle',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='Doppel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='Sinq Malt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='St.George',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='new',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='Name',
            field=models.ManyToManyField(to='Company.Product'),
        ),
    ]
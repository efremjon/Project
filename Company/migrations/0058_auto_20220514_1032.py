# Generated by Django 3.2.9 on 2022-05-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0057_remove_product_amount_in_store_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Castle',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Doppel',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Sinq Malt',
        ),
        migrations.RemoveField(
            model_name='product',
            name='St.George',
        ),
        migrations.RemoveField(
            model_name='product',
            name='new',
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='Castle',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='Doppel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='Sinq Malt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='St.George',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='new',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.9 on 2022-05-13 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0045_auto_20220512_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_amount_in_store',
            name='Store',
        ),
        migrations.AddField(
            model_name='product_amount_in_store',
            name='Store',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company_store'),
        ),
    ]

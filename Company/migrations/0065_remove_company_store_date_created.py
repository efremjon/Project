# Generated by Django 3.2.9 on 2022-05-14 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0064_alter_company_store_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_store',
            name='date_created',
        ),
    ]

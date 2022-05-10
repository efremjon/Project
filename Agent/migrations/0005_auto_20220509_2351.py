# Generated by Django 3.2.9 on 2022-05-10 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0004_store_manager'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store_manager',
            old_name='Stor',
            new_name='Store',
        ),
        migrations.AddField(
            model_name='store_manager',
            name='Adderes',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='store_manager',
            name='about',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='store_manager',
            name='phone1',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0038_auto_20220511_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='company_store',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='Location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
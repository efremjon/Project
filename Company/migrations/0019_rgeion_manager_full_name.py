# Generated by Django 3.2.9 on 2022-05-02 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0018_admin_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='rgeion_manager',
            name='Full_Name',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

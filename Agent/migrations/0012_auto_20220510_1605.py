# Generated by Django 3.2.9 on 2022-05-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0011_agent_order_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Rooting',
            new_name='Routing',
        ),
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Profile/'),
        ),
    ]

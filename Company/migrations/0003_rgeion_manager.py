# Generated by Django 3.2.9 on 2022-05-01 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0002_alter_region_region_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rgeion_Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('Adderes', models.CharField(max_length=200, null=True)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('Telegram', models.CharField(max_length=200, null=True)),
                ('facebook', models.CharField(max_length=200, null=True)),
                ('instagrm', models.CharField(max_length=200, null=True)),
                ('Region', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.region')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

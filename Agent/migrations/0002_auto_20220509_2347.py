# Generated by Django 3.2.9 on 2022-05-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='License',
            field=models.FileField(blank=True, null=True, upload_to='License'),
        ),
        migrations.AddField(
            model_name='customer',
            name='TIN_NO',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='agreement',
            field=models.FileField(blank=True, null=True, upload_to='Agreement'),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
# Generated by Django 3.2.9 on 2022-05-02 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0014_auto_20220501_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='License',
            field=models.ImageField(blank=True, null=True, upload_to='license'),
        ),
    ]

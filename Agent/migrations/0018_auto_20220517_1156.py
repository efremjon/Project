# Generated by Django 3.2.9 on 2022-05-17 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0017_product_in_agent_stor_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent_order',
            name='Payment_Opetion',
        ),
        migrations.RemoveField(
            model_name='agent_order',
            name='product',
        ),
        migrations.AddField(
            model_name='agent_order',
            name='Castle',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent_order',
            name='Doppel',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent_order',
            name='Sinq_Malt',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent_order',
            name='St_George',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent_order',
            name='new',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='agent_order',
            name='newone',
            field=models.IntegerField(default=0),
        ),
    ]

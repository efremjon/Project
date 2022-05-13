# Generated by Django 3.2.9 on 2022-05-12 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0042_rename_product_name_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Amount_in_Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Quintitiy', models.CharField(max_length=200, null=True)),
                ('Product_Name', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.product')),
                ('Store', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company.company_store')),
            ],
        ),
    ]
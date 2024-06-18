# Generated by Django 5.0.6 on 2024-06-18 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_category_alter_product_slug_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='myapp.category'),
        ),
    ]

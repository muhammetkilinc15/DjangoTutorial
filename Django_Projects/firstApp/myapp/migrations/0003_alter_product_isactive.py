# Generated by Django 5.0.6 on 2024-06-17 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_category_product_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]

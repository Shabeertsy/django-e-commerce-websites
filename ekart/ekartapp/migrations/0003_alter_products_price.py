# Generated by Django 4.1.4 on 2023-01-21 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ekartapp", "0002_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.IntegerField(),
        ),
    ]

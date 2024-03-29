# Generated by Django 4.1.4 on 2023-01-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ekartapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("area", models.CharField(max_length=255)),
                ("pincode", models.IntegerField()),
                ("district", models.CharField(max_length=255)),
                ("state", models.CharField(max_length=255)),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshop", "0012_banner"),
    ]

    operations = [
        migrations.CreateModel(
            name="BannerRotationInterval",
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
                ("interval_seconds", models.PositiveIntegerField(default=3000)),
            ],
        ),
        migrations.RemoveField(
            model_name="banner",
            name="interval_seconds",
        ),
    ]

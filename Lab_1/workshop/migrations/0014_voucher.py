# Generated by Django 4.2.5 on 2023-11-21 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshop", "0013_bannerrotationinterval_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Voucher",
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
                ("code", models.CharField(max_length=20, unique=True)),
                ("description", models.TextField()),
                ("discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("max_usages", models.PositiveIntegerField()),
                ("usage_count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]

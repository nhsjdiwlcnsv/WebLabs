# Generated by Django 4.2.5 on 2023-09-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("workshop", "0006_question_alter_order_created_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="title",
            new_name="question",
        ),
        migrations.RemoveField(
            model_name="question",
            name="description",
        ),
        migrations.AddField(
            model_name="question",
            name="answer",
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
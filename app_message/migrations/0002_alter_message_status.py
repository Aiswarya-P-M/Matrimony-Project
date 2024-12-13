# Generated by Django 5.1.3 on 2024-11-18 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_message", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="message",
            name="status",
            field=models.CharField(
                choices=[("read", "Read"), ("unread", "Unread")],
                default="unread",
                max_length=10,
            ),
        ),
    ]

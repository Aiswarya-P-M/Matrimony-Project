# Generated by Django 5.1.3 on 2024-12-03 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_subscription", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="start_date",
        ),
        migrations.AddField(
            model_name="subscription",
            name="duration",
            field=models.CharField(
                choices=[
                    ("30 days", "30 days"),
                    ("120 days", "120 days"),
                    ("365 days", "365 days"),
                ],
                default=1,
                max_length=10,
            ),
            preserve_default=False,
        ),
    ]
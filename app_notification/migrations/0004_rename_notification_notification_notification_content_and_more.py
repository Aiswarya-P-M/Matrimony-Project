# Generated by Django 5.1.3 on 2024-11-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_notification", "0003_alter_notification_receiver_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="notification",
            old_name="notification",
            new_name="notification_content",
        ),
        migrations.AddField(
            model_name="notification",
            name="notification_title",
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]

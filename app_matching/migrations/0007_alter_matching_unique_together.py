# Generated by Django 5.1.3 on 2024-11-15 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app_matching", "0006_alter_matching_user1_alter_matching_user2_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="matching",
            unique_together=set(),
        ),
    ]
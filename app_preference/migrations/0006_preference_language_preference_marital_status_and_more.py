# Generated by Django 5.1.3 on 2024-11-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_preference", "0005_rename_age_max_preference_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="preference",
            name="Language",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="preference",
            name="Marital_status",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Age",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Education",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Height",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Income",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Location",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Profession",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="preference",
            name="Weight",
            field=models.JSONField(blank=True, null=True),
        ),
    ]

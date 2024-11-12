# Generated by Django 5.1.3 on 2024-11-11 11:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Preference",
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
                ("Age", models.IntegerField(blank=True, null=True)),
                ("Profession", models.CharField(blank=True, max_length=100, null=True)),
                ("Education", models.CharField(blank=True, max_length=100, null=True)),
                ("Location", models.CharField(blank=True, max_length=100, null=True)),
                ("Caste", models.CharField(blank=True, max_length=50, null=True)),
                ("Religion", models.CharField(blank=True, max_length=50, null=True)),
                ("Income", models.IntegerField(blank=True, null=True)),
                ("Height", models.IntegerField(blank=True, null=True)),
                ("Weight", models.IntegerField(blank=True, null=True)),
                ("Gender", models.CharField(blank=True, max_length=50, null=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

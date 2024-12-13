# Generated by Django 5.1.3 on 2024-11-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_commonmatching", "0003_mastertable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commonmatchingtable",
            name="type",
            field=models.CharField(
                choices=[
                    ("gender", "Gender"),
                    ("age", "Age"),
                    ("caste", "Caste"),
                    ("religion", "Religion"),
                    ("profession", "Profession"),
                    ("income", "Income"),
                    ("education", "Education"),
                    ("height", "Height"),
                    ("weight", "Weight"),
                    ("location", "Location"),
                    ("language", "Language"),
                    ("marital_status", "Marital_status"),
                ],
                max_length=20,
                unique=True,
            ),
        ),
    ]

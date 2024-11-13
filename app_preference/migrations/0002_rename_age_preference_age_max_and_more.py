# Generated by Django 5.1.3 on 2024-11-13 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_commonmatching", "0005_alter_commonmatchingtable_type"),
        ("app_preference", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="preference",
            old_name="Age",
            new_name="Age_max",
        ),
        migrations.RenameField(
            model_name="preference",
            old_name="Height",
            new_name="Height_max",
        ),
        migrations.RenameField(
            model_name="preference",
            old_name="Income",
            new_name="Income_max",
        ),
        migrations.RenameField(
            model_name="preference",
            old_name="Weight",
            new_name="Weight_max",
        ),
        migrations.AddField(
            model_name="preference",
            name="Age_min",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="preference",
            name="Height_min",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="preference",
            name="Income_min",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="preference",
            name="Weight_min",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name="preference",
            name="Education",
        ),
        migrations.RemoveField(
            model_name="preference",
            name="Location",
        ),
        migrations.RemoveField(
            model_name="preference",
            name="Profession",
        ),
        migrations.AddField(
            model_name="preference",
            name="Education",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"type__type": "education"},
                related_name="preferences_education",
                to="app_commonmatching.mastertable",
            ),
        ),
        migrations.AddField(
            model_name="preference",
            name="Location",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"type__type": "location"},
                related_name="preferences_location",
                to="app_commonmatching.mastertable",
            ),
        ),
        migrations.AddField(
            model_name="preference",
            name="Profession",
            field=models.ManyToManyField(
                blank=True,
                limit_choices_to={"type__type": "profession"},
                related_name="preferences_profession",
                to="app_commonmatching.mastertable",
            ),
        ),
    ]
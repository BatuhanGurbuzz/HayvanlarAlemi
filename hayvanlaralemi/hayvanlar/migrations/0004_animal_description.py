# Generated by Django 5.0.1 on 2024-01-27 10:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hayvanlar", "0003_alter_animal_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="description",
            field=models.TextField(
                max_length=255, null=True, verbose_name="Hayvan Açıklaması"
            ),
        ),
    ]

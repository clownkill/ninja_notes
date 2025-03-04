# Generated by Django 5.1.6 on 2025-03-04 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=300)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "Категории",
                "ordering": ("created",),
            },
        ),
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(max_length=250)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("completed", models.BooleanField(blank=True, default=False)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="notes.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Заметки",
                "ordering": ("-created",),
            },
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-25 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ApplyJob",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Accepted", "Accepted"),
                            ("Declined", "Declined"),
                            ("Pending", "Pending"),
                        ],
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Industry",
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
                ("name", models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("city", models.CharField(max_length=100)),
                ("salary", models.PositiveIntegerField(default=40000)),
                ("requirements", models.TextField()),
                ("ideal_candidate", models.TextField()),
                ("is_available", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "job_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Remote", "Remote"),
                            ("Onsite", "Onsite"),
                            ("hybrid", "hybrid"),
                        ],
                        max_length=30,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="State",
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
                ("name", models.CharField(max_length=70)),
            ],
        ),
    ]

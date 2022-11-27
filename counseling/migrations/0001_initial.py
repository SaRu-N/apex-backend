# Generated by Django 3.2.13 on 2022-11-16 08:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import accounts.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Counseling",
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
                (
                    "student_name",
                    models.CharField(max_length=100, verbose_name="student_name"),
                ),
                ("note", models.CharField(max_length=150, verbose_name="note")),
                (
                    "phone_number",
                    models.CharField(
                        max_length=50,
                        validators=[accounts.validators.PhoneNumberValidator()],
                        verbose_name="phone_number",
                    ),
                ),
                ("date", models.DateField(verbose_name="date")),
                (
                    "counsellor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="counsellor",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Counseling",
                "verbose_name_plural": "Counselings",
            },
        ),
    ]

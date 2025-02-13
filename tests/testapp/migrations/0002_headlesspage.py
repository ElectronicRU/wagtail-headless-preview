# Generated by Django 3.2.11 on 2022-01-29 00:00

import django.db.models.deletion
import wagtail_headless_preview.models

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailcore", "0066_collection_management_permissions"),
        ("wagtail_headless_preview_tests", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HeadlessPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(wagtail_headless_preview.models.HeadlessMixin, "wagtailcore.page"),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-02 11:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("recipename", models.TextField(max_length=100)),
                (
                    "recipeimg",
                    models.ImageField(
                        default="no_recipe_img.png", upload_to="recipe_images"
                    ),
                ),
                ("description", models.TextField(blank=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(2023, 7, 2, 17, 16, 29, 411137)
                    ),
                ),
                ("no_of_likes", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                ("bio", models.TextField(blank=True)),
                (
                    "profileimg",
                    models.ImageField(
                        default="blank-profile-picture.png", upload_to="profile_images"
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=100)),
                (
                    "last_updated",
                    models.DateField(
                        default=datetime.datetime(2023, 7, 2, 17, 16, 29, 411137)
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

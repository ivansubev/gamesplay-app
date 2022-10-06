from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()
    age = models.IntegerField(
        validators=(
            MinValueValidator(AGE_MIN_VALUE),
        )
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class GameModel(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5
    MAX_LEVEL_MIN_VALUE = 1
    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=(
            ("Action", "Action"),
            ("Adventure", "Adventure"),
            ("Puzzle", "Puzzle"),
            ("Strategy", "Strategy"),
            ("Sports", "Sports"),
            ("Board/Card Game", "Board/Card Game"),
            ("Other", "Other"),
        )
    )
    rating = models.FloatField(
        validators=(
            MinValueValidator(RATING_MIN_VALUE),
            MaxValueValidator(RATING_MAX_VALUE),
        )
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MAX_LEVEL_MIN_VALUE),
        )
    )
    image_url = models.URLField()
    summary = models.TextField(
        null=True,
        blank=True
    )

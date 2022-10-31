from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from exam_web_basics.web.validators import min_2_chars, year_validator


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_VALUE = 2

    AGE_MIN_VALUE = 18
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            min_2_chars,
        ]

    )

    email = models.EmailField()

    age = models.IntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE),
        ]
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LEN,
    )

    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=FIRST_NAME_MAX_LEN,

    )

    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=LAST_NAME_MAX_LEN,

    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    CAR_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    PRICE_MIN_VALUE = 1.0

    SPORTS_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHER = "Other"

    CAR_TYPES = (
        (SPORTS_CAR, SPORTS_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHER, OTHER),
    )

    type = models.CharField(
        max_length=CAR_MAX_LEN,
        choices=CAR_TYPES,
    )

    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=[
            MinLengthValidator(MODEL_MIN_LEN),
        ]
    )

    year = models.IntegerField(
        validators=[
            year_validator,
        ]
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]
    )

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

from regular_exam.profiles.models import Profile


class Car(models.Model):
    MAX_TYPE_LENGTH = 10

    MAX_MODEL_LENGTH = 15
    MIN_MODEL_LENGTH = 1

    MIN_PRICE_VALUE = 1.0
    MIN_YEAR = 1999
    MAX_YEAR = 2030

    ERROR_MESSAGE_YEAR = f"Year must be between {MIN_YEAR} and {MAX_YEAR}!"

    TYPE_RALLY = "Rally"
    TYPE_OPEN_WHEEL = "Open-wheel"
    TYPE_KART = "Kart"
    TYPE_DRAG = "Drag"
    TYPE_OTHER = "Other"

    TYPES = (
        (TYPE_RALLY, TYPE_RALLY),
        (TYPE_OPEN_WHEEL, TYPE_OPEN_WHEEL),
        (TYPE_KART, TYPE_KART),
        (TYPE_DRAG, TYPE_DRAG),
        (TYPE_OTHER, TYPE_OTHER),
    )

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        blank=False,
        null=False,
        choices=TYPES,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[MinLengthValidator(MIN_MODEL_LENGTH)],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            MinValueValidator(MIN_YEAR, message=ERROR_MESSAGE_YEAR),
            MaxValueValidator(MAX_YEAR, message=ERROR_MESSAGE_YEAR),
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={'unique': "This image URL is already in use! Provide a new one."},
        verbose_name='Image URL'
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(MIN_PRICE_VALUE)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

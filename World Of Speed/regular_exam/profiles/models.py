from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from regular_exam.profiles.validators import validate_username


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 3

    MAX_PASSWORD_LENGTH = 20

    MAX_FIRST_NAME_LENGTH = 25

    MAX_LAST_NAME_LENGTH = 25

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinLengthValidator(
                MIN_USERNAME_LENGTH,
                message=f"Username must be at least {MIN_USERNAME_LENGTH} characters long."),
            validate_username,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=[MinValueValidator(21)],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture',
    )

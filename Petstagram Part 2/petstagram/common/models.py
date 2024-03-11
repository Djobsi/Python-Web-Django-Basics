from django.db import models

from petstagram.photos.models import PetPhoto


class Comment(models.Model):
    text = models.TextField(
        max_length=300,
        null=False,
        blank=False
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.RESTRICT,
    )


class PhotoLike(models.Model):
    pet_photo = models.ForeignKey(
        PetPhoto,
        on_delete=models.DO_NOTHING,
    )

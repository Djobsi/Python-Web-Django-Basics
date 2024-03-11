from django.db import models
from django.utils.text import slugify
import uuid


def get_random_hash():
    return uuid.uuid1().hex[-4:]


def generate_slug(*args, **kwargs):
    return get_random_hash()


class Todo(models.Model):
    MAX_LENGTH_TITLE = 24
    MAX_TENANT_LENGTH = 16

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
        null=False,
        blank=False,
    )

    description = models.TextField()

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    slug = models.SlugField(
        editable=False,
        default=generate_slug,
    )

    tenant = models.CharField(
        max_length=MAX_TENANT_LENGTH,
        null=True,
        blank=True,
        default=None,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title) + ' ' + get_random_hash()
        return super().save(*args, **kwargs)

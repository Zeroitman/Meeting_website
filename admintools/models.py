from django.db import models
from django.utils import timezone


class CoreModel(models.Model):
    created = models.DateTimeField(
        'Created',
        null=False,
        default=timezone.now,
        editable=False,
    )

    updated = models.DateTimeField(
        'Updated',
        null=False,
        default=timezone.now,
        editable=False,
    )

    class Meta:
        abstract = True
        ordering = ['-updated']

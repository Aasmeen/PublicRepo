from django.db import models

from apps.core.models import TimeStampedModel


class Album(TimeStampedModel):
    title = models.CharField(max_length=200)

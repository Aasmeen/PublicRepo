from django.db import models

from apps.core.models import TimeStampedModel

# Create your models here.

class Album(TimeStampedModel):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)


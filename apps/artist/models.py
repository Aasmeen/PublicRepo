from django.db import models

from apps.core.models import TimeStampedModel


class Artist(TimeStampedModel):
    name = models.CharField(max_length=255, help_text="Name of the Artist")

    def __str__(self):
        return f"{self.name}"
    
    @property
    def track_count(self):
        self.tracks.count()

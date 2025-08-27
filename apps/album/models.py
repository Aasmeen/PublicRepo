from django.db import models

from apps.core.models import TimeStampedModel


class Album(TimeStampedModel):
    title = models.CharField(max_length=255)
    release_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, help_text="Album description")

    def __str__(self) -> str:
        return f"{self.title} - {self.artist.name}"
    
    @property
    def track_count(self):
        self.tracks.count()

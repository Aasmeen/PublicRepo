from django.core.validators import MinValueValidator
from django.db import models

from apps.album.models import Album
from apps.artist.models import Artist
from apps.core.models import TimeStampedModel


class Track(TimeStampedModel):
    name = models.CharField(max_length=255, help_text="Name of the track")
    artist = models.ManyToManyField(Artist, related_name="tracks")
    album = models.ForeignKey(Album, related_name="tracks", on_delete=models.SET_NULL, null=True)
    release_date = models.DateTimeField(auto_now_add=True)
    duration = models.PositiveIntegerField(
        validators=[MinValueValidator(20)], help_text="Duration of the track in sec"
    )

    def __str__(self) -> str:
        return f"{self.name}: ({self.album.title})" 

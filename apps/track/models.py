from django.core.validators import MinValueValidator
from django.db import models
from rest_framework.exceptions import ValidationError

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
    album_order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], help_text="Ordering in the album"
    )

    class Meta:
        unique_together = ['album', 'album_order']
        ordering = ['album', 'album_order']

    def __str__(self) -> str:
        return f"{self.name}: ({self.album.title})" 
    
    def clean(self) -> None:
        if Track.objects.filter(
            album_id=self.album.id,
            album_order=self.album_order
        ).exclude(id=self.id).exists():
            raise ValidationError(
                f"Track number {self.track_number} already exists in this album."
            )

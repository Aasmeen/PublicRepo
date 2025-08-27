from django.contrib.auth.models import User
from django.db import models
from rest_framework.exceptions import ValidationError

from apps.core.models import TimeStampedModel
from apps.track.models import Track

class PlayList(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="Playlist name")

    class Meta:
        unique_together = ['user', 'name']

    def clean(self):
        if PlayList.objects.filter(
            user=self.user, name=self.name
        ).exclude(id=self.id).exists():
            raise ValidationError("A user cannot have same plalist name")

class PlaylistTracks(TimeStampedModel):
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['playlist', 'track']

    def clean(self):
        if PlaylistTracks.objects.filter(
            playlist=self.playlist,
            track=self.track
        ).exists():
            raise ValidationError("A track cannot be added again to same playlist")

    

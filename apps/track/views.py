from rest_framework.viewsets import ModelViewSet

from apps.track.models import Track
from apps.track.serializer import TrackSerializer


class TrackViewSets(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

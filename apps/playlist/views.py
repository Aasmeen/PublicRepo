from rest_framework.viewsets import ModelViewSet
from apps.playlist.models import PlayList, PlaylistTracks
from apps.playlist.serializer import PlayListSerializer, PlayListTrackSerializer

class PlayListViewSet(ModelViewSet):
    queryset = PlayList.objects.all()
    serializer_class = PlayListSerializer


class PlayListTrackViewSet(ModelViewSet):
    queryset = PlaylistTracks.objects.all()
    serializer_class = PlayListTrackSerializer

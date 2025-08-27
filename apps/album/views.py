from rest_framework.viewsets import ModelViewSet

from apps.album.models import Album
from apps.album.serializer import AlbumSerializer


class AlbumViewSets(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

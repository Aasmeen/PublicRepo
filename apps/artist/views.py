from rest_framework.viewsets import ModelViewSet

from apps.artist.models import Artist
from apps.artist.serializers import ArtistSerializer


class ArtistViewSets(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

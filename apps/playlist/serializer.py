from rest_framework.serializers import ModelSerializer

from apps.playlist.models import PlayList, PlaylistTracks

class PlayListSerializer(ModelSerializer):
    class Meta:
        model = PlayList
        fields = '__all__'


class PlayListTrackSerializer(ModelSerializer):
    class Meta:
        model = PlaylistTracks
        fields = '__all__'

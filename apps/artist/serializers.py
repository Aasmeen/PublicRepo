from rest_framework.serializers import ModelSerializer

from apps.artist.models import Artist


class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.artist.views import ArtistViewSets

artist_router = DefaultRouter()
artist_router.register(r'artist', ArtistViewSets)

urlpatterns = [
    path('', include(artist_router.urls))
]
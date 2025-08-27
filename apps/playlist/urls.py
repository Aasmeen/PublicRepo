from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.playlist.views import PlayListTrackViewSet, PlayListViewSet

playlist_router = DefaultRouter()
playlist_router.register(r'playlist', PlayListViewSet)

playlist_track_router = DefaultRouter()
playlist_track_router.register(r'playlist-track', PlayListTrackViewSet)

urlpatterns = [
    path('', include(playlist_router.urls)),
    path('', include(playlist_track_router.urls)),
]

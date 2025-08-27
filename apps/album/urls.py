from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.album.views import AlbumViewSets

album_router = DefaultRouter()
album_router.register(r'album', AlbumViewSets)

urlpatterns = [
    path('', include(album_router.urls))
]
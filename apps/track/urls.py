from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.track.views import TrackViewSets

track_router = DefaultRouter()
track_router.register(r'track', TrackViewSets)

urlpatterns = [
    path('', include(track_router.urls))
]
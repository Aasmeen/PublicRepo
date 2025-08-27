from django.contrib import admin

from apps.playlist.models import PlayList, PlaylistTracks


admin.site.register(PlayList)
admin.site.register(PlaylistTracks)

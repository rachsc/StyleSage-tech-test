from django.contrib import admin
from .models import Artist, Album, Composer, MediaType, Genre, Track

# I register my models in my admin so I am able to inspect in my django admin interface


class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]


class AlbumAdmin(admin.ModelAdmin):
    list_display = ["title", "artist"]


class ComposerAdmin(admin.ModelAdmin):
    list_display = ["composer"]


class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


class TrackAdmin(admin.ModelAdmin):
    list_display = ["title", "album", "media_type", "genre", "composer_name", "milliseconds", "byte_s"]


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)

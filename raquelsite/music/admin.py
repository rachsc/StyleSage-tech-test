from django.contrib import admin
from .models import Artist, Album, Composer, MediaType, Genre, Track

# I register my models in my admin so I am able to inspect in my django admin interface


class ArtistAdmin(admin.ModelAdmin):
    list_display = '__all__'


class AlbumAdmin(admin.ModelAdmin):
    list_display = '__all__'


class ComposerAdmin(admin.ModelAdmin):
    list_display = '__all__'


class MediaTypeAdmin(admin.ModelAdmin):
    list_display = '__all__'


class GenreAdmin(admin.ModelAdmin):
    list_display = '__all__'


class TrackAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)

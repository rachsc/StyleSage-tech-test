from rest_framework import serializers
# from .models import Artist, Album, Composer, MediaType, Genre, Track
from .models import Artist, Album, Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'artist_id']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['title', 'album_id', 'artist']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['track_id', 'name', 'album', 'milliseconds']

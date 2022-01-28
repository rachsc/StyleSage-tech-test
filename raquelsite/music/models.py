from django.db import models
from django.urls import reverse
from django.db.models import Count


class Artist(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)
    artist_id = models.AutoField(db_column='ArtistId', primary_key=True)

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'pk': self.artist_id})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artists'
        ordering = ('name',)


# class MusicArtist(models.Model):
#     name = models.CharField(max_length=200)
#
#     class Meta:
#         db_table = 'music_artist'


class Album(models.Model):
    title = models.TextField(db_column='Title')
    album_id = models.AutoField(db_column='AlbumId', primary_key=True)
    # artist = models.IntegerField(db_column='ArtistId')
    artist = models.ForeignKey(Artist, models.DO_NOTHING, related_name='related_albums')

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'pk': self.album_id})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'albums'
        ordering = ('title',)

    @property
    def album_artist(self):
        return self.artist

    def tracks_count(self):
        return self.related_tracks.count()

    def album_duration(self):
        duration_ms = 0
        for ms in self.related_tracks.values_list('milliseconds', flat=True):
            duration_ms = duration_ms + ms
        duration_min = duration_ms/(1000*60)
        duration_min_2decimals = float("{:.2f}".format(duration_min))
        return duration_min_2decimals

    def longest_track_duration(self):
        longest_min = (max(self.related_tracks.values_list('milliseconds', flat=True)))/(1000*60)
        return float("{:.2f}".format(longest_min))

    def shortest_track_duration(self):
        shortest_min = (min(self.related_tracks.values_list('milliseconds', flat=True))) / (1000 * 60)
        return float("{:.2f}".format(shortest_min))


# class MusicAlbum(models.Model):
#     title = models.CharField(max_length=200)
#     artist = models.ForeignKey('MusicArtist', models.DO_NOTHING)
#
#     class Meta:
#         db_table = 'music_album'


class Track(models.Model):
    track_id = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=0, related_name='related_tracks')
    # album = models.IntegerField(db_column='AlbumId', blank=True, null=True)
    # composer = models.TextField(db_column='Composer', blank=True, null=True)
    milliseconds = models.IntegerField(db_column='Milliseconds')

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tracks'
        ordering = ('name',)


# class MusicTrack(models.Model):
#     title = models.CharField(max_length=200)
#     milliseconds = models.PositiveIntegerField()
#     album = models.ForeignKey(MusicAlbum, models.DO_NOTHING)
#
#     class Meta:
#         db_table = 'music_track'



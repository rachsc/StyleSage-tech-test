from django.db import models


class Artist(models.Model):
    name = models.TextField(db_column='Name', blank=True, null=True)
    artist_id = models.AutoField(db_column='ArtistId', primary_key=True)

    objects = models.Manager()

    @property
    def albums(self):
        return self.album_set.all()

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
    artist = models.ForeignKey(Artist, models.DO_NOTHING)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'albums'
        ordering = ('title',)


# class MusicAlbum(models.Model):
#     title = models.CharField(max_length=200)
#     artist = models.ForeignKey('MusicArtist', models.DO_NOTHING)
#
#     class Meta:
#         db_table = 'music_album'


class Track(models.Model):
    track_id = models.AutoField(db_column='TrackId', primary_key=True)
    name = models.TextField(db_column='Name')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=0)
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



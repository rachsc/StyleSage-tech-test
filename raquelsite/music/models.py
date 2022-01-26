from django.db import models


class Artist(models.Model):
    # artistid = models.AutoField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=200)  # Field name made lowercase. This field type is a guess.

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Album(models.Model):
    # albumid = models.AutoField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class Composer(models.Model):
    composer = models.CharField(max_length=30)

    def __str__(self):
        return self.composer

    class Meta:
        ordering = ('composer',)


class MediaType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Track(models.Model):
    title = models.CharField(max_length=200)  # Field name made lowercase. This field type is a guess.
    composer = models.ManyToManyField(Composer)
    album = models.ForeignKey(Album, models.PROTECT)
    media_type = models.ForeignKey(MediaType, models.PROTECT)
    genre = models.ForeignKey(Genre, models.PROTECT)
    composer_name = models.CharField(max_length=220, default=None, blank=True, null=True)
    milliseconds = models.PositiveIntegerField(default=0)
    byte_s = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

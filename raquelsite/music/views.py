# from rest_framework import parsers
# from rest_framework import response
# from rest_framework import status
# from rest_framework import viewsets
#
# from .models import Artist
# from .serializers import ArtistSerializer
#
#
# class ArtistViewSet(viewsets.ModelViewSet):
#     serializer_class = ArtistSerializer
#     queryset = Artist.objects.all()

from django.shortcuts import render

from .models import Artist, Album, Track


def index(request):
    return render(request, 'base.html')


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})


def artist_detail(request, pk):
    artist = Artist.objects.get(artist_id=pk)
    return render(request, 'artist_detail.html', {'artist': artist})


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album_list.html', {'albums': albums})


def album_detail(request, pk):
    album = Album.objects.get(album_id=pk)
    return render(request, 'album_detail.html', {'album': album})
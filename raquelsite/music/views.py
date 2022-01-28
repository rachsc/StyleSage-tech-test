# from django.shortcuts import render
# from .models import Artist, Album, Track
#
#
# def index(request):
#     return render(request, 'base.html')
#
#
# def artist_list(request):
#     artists = Artist.objects.all()
#     return render(request, 'artist_list.html', {'artists': artists})
#
#
# def artist_detail(request, pk):
#     artist = Artist.objects.get(artist_id=pk)
#     return render(request, 'artist_detail.html', {'artist': artist})
#
#
# def album_list(request):
#     albums = Album.objects.all()
#     return render(request, 'album_list.html', {'albums': albums})
#
#
# def album_detail(request, pk):
#     album = Album.objects.get(album_id=pk)
#     return render(request, 'album_detail.html', {'album': album})


from django.views import generic
from django.shortcuts import render
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Artist, Album


def total_duration(queryset):
    duration = 0
    for track in queryset:
        duration = duration + track.milliseconds
    return duration


def index(request):
    return render(request, 'base.html')


class ArtisListView(generic.ListView):
    model = Artist
    context_object_name = 'artists'
    queryset = Artist.objects.all()
    template_name = 'artist_list.html'


class ArtistDetailView(generic.DetailView):
    model = Artist
    context_object_name = 'artist'
    template_name = 'artist_detail.html'


class AlbumListView(generic.ListView):
    model = Album
    context_object_name = 'albums'
    queryset = Album.objects.all()
    template_name = 'album_list.html'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     data = super(AlbumListView, self).get_context_data(**kwargs)
    #     data['album_artist'] = self.model.album_artist
    #     data['album_duration'] = self.model.album_duration
    #     return data


class AlbumDetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'album_detail.html'










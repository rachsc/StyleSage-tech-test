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
import csv
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Artist, Album, ArtistImage
from .forms import ArtistImageForm, UserForm


def download_artists(request, queryset):
    model = queryset.model
    model_fields = model._meta.fields + model._meta.many_to_many
    field_names = [field.name for field in model_fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="artists.csv"'

    # the csv writer
    writer = csv.writer(response, delimiter=";")
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for row in queryset:
        values = []
        for field in field_names:
            value = getattr(row, field)
            if callable(value):
                try:
                    value = value() or ''
                except:
                    value = 'Error retrieving value'
            if value is None:
                value = ''
            values.append(value)
        writer.writerow(values)
    return response


def export_artists(request):
    # Create the HttpResponse object with the appropriate CSV header.
    data = download_artists(request, Artist.objects.all())
    response = HttpResponse(data, content_type='text/csv')
    return response


def upload_images(request):
    if request.method == "POST":
        form = ArtistImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("upload")
    form = ArtistImageForm()
    images = ArtistImage.objects.all()
    return render(request=request, template_name="upload.html", context={'form': form, 'images': images})


def index(request):
    return render(request, 'base.html')


class ArtistListView(generic.ListView):
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


class AlbumDetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'album_detail.html'


class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # Show blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # Submit user registration
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()  # Creates an object from the form but does not save it to the database yet

            # # cleaned (normalized) data
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user.set_password(password)  # This is the way to change the default password
            # user.save()
            #
            # # returns User objects if credentials are correct
            # user = authenticate(username=username, password=password)  # check if it exist in the database
            #
            # if user is not None:
            #     if user.is_active:  # User is not banned or something
            #         login(request, user)
            return redirect('index')

        return render(request, self.template_name, {'form': form})

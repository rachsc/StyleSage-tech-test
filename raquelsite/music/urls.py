from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('artists/', views.ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
    path('download-artists/', views.export_artists, name='download-artists'),
    path('upload/', views.upload_images, name='upload'),
]
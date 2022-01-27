from django.urls import path, include
from . import views
from rest_framework import routers

# app_name = "music"
# router = routers.DefaultRouter()
# router.register(r'artist', views.ArtistViewSet, basename='artist')

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index, name='index'),
    path('artists/', views.ArtisListView.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetailView.as_view(), name='artist_detail'),
    path('albums/', views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>', views.AlbumDetailView.as_view(), name='album_detail'),
]
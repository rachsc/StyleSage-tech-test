from django.urls import path, include
from . import views
from rest_framework import routers

# app_name = "music"
# router = routers.DefaultRouter()
# router.register(r'artist', views.ArtistViewSet, basename='artist')

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index, name='index'),
    path('artists/', views.artist_list, name='artist_list'),
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
]
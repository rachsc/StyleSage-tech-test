from django.urls import path, include
from . import views
from rest_framework import routers

app_name = "music"
router = routers.DefaultRouter()
router.register(r'artist', views.ArtistViewSet, basename='artist')

urlpatterns = [
    path('', include(router.urls)),
]
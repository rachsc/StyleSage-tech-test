from rest_framework import parsers
from rest_framework import response
from rest_framework import status
from rest_framework import viewsets

from .models import Artist
from .serializers import ArtistSerializer
from .serializers import ArtistSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()




from django import forms
from .models import Artist, ArtistImage


class ArtistImageForm(forms.ModelForm):
    class Meta:
        model = ArtistImage
        fields = ['image', 'name']


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ArtistImage


class ArtistImageForm(forms.ModelForm):
    class Meta:
        model = ArtistImage
        fields = ['image', 'name']


class PassphraseForm(forms.Form):
    passphrase = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 10, 'cols': 80}))



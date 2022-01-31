from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ArtistImage


# class UserForm(UserCreationForm):
#     # password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password1']


class ArtistImageForm(forms.ModelForm):
    class Meta:
        model = ArtistImage
        fields = ['image', 'name']



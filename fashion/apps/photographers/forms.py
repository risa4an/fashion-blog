from django import forms

from .models import Photographer, Photo

class PostForm(forms.ModelForm):
    class Meta:
        model = Photographer
        fields = ('name', 'discription',)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo_image', 'photo_name', )
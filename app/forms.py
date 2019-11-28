from django.forms import ModelForm

from app.models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'comment', 'image', 'category']

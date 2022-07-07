from django.forms import ModelForm
from album.models import Album
from picture.forms import PictureForm

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ["picture"]


class AlbumEditForm(ModelForm):
    class Meta:
        model = Album
        fields = ["title", "description", "cover"]
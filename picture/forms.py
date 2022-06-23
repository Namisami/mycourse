from django.forms import ModelForm, TextInput, Textarea, ImageField
from album.models import Album
from picture.models import Picture

class PictureForm(ModelForm):
    # photo_file = ImageField(Picture)
    class Meta:
        model = Picture
        # fields = ["picture"]
        fields = ["photo_file"]
        # ["photo_file", "author", "category", "description"]
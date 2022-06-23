from django.forms import ModelForm, TextInput, Textarea, ImageField
from album.models import Album
from picture.models import Picture
from picture.forms import PictureForm

class AlbumForm(ModelForm):
    # photo_file = ImageField(Picture)
    class Meta:
        model = Album
        fields = ["picture"]
        # fields = ["photo_file"]
        # ["photo_file", "author", "category", "description"]

        # widgets = {
        #     "title": TextInput(attrs={
        #         'placeholder': "Введите название"
        #     }),
        #     "description": Textarea(attrs={
        #         'placeholder': "Введите описание"
        #     }),
        #     "cover": ImageField(),
        #     "picture": ImageField(),
        # }
from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea, ImageField
from album.models import Album
from picture.models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["photo_file"]
    def __init__(self, *args, **kwargs):
        super(PictureForm, self).__init__(*args, **kwargs)
        self.fields['photo_file'].widget.attrs.update({
            'class': 'main__input main__photo',
        })


class PictureMainEditForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["author", "category", "description"]

class PictureSubcategoryEditForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["subcategory"]
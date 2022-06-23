from dataclasses import fields
from django.forms import ModelForm, TextInput, Textarea, ImageField
from album.models import Album
from picture.models import Picture

class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["photo_file"]


class PictureMainEditForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["author", "category", "description"]

class PictureSubcategoryEditForm(ModelForm):
    class Meta:
        model = Picture
        fields = ["subcategory"]
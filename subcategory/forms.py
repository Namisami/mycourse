from django.forms import ModelForm, TextInput, Textarea, ImageField
from subcategory.models import Subcategory

class SubcategoryForm(ModelForm):
    class Meta:
        model = Subcategory
        fields = ["category"]
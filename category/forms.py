from django.forms import ModelForm, TextInput, Textarea, ImageField
from category.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["title", "description"]
    # def __init__(self, *args, **kwargs):
    #     super(CategoryForm, self).__init__(*args, **kwargs)
    #     self.fields['photo_file'].widget.attrs.update({
    #         'class': 'new__input',
    #     })


# class CategoryMainEditForm(ModelForm):
#     class Meta:
#         model = Category
#         fields = ["author", "category", "description"]


# class CategorySubcategoryEditForm(ModelForm):
#     class Meta:
#         model = Category
#         fields = ["subcategory"]
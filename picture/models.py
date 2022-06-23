from distutils.command.upload import upload
from tokenize import blank_re
from unicodedata import category
from django.db import models
from author.models import Author
from category.models import Category

class Picture(models.Model):
    photo_file = models.ImageField(verbose_name="Изображение", upload_to="pictures", blank=True)
    author = models.ForeignKey(verbose_name="Автор", to=Author, on_delete=models.CASCADE, null=True, blank=True)
    upload_date = models.DateField(verbose_name="Дата загрузки", auto_now_add=True, blank=True)
    category = models.ForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    def __str__(self):
        return str(self.id)
        
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
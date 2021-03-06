from django.db import models
from author.models import Author
from category.models import Category
from subcategory.models import Subcategory
from authentication.models import User

class Picture(models.Model):
    photo_file = models.ImageField(verbose_name="Изображение", upload_to="pictures", blank=True)
    author = models.ForeignKey(verbose_name="Автор", to=Author, on_delete=models.CASCADE, null=True, blank=True)
    upload_date = models.DateField(verbose_name="Дата загрузки", auto_now_add=True, blank=True)
    category = models.ForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ManyToManyField(verbose_name="Подкатегории", to=Subcategory, blank=True)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    owner = models.ForeignKey(verbose_name="Владелец", to=User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
        
    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
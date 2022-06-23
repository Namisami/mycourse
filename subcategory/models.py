from django.db import models
from category.models import Category

class Subcategory(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
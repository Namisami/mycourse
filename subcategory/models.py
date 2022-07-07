from django.db import models
from category.models import Category
from authentication.models import User

class Subcategory(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание")
    category = models.ForeignKey(verbose_name="Категория", to=Category, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(verbose_name="Владелец", to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
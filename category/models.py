from django.db import models
from authentication.models import User

class Category(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(to=User, verbose_name="Владелец", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
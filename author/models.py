from operator import mod
from django.db import models
from pkg_resources import require

class Author(models.Model):
    nickname = models.CharField(verbose_name="Никнейм", max_length=255)
    bio = models.TextField(verbose_name="О авторе", blank=True)

    def __str__(self):
        return self.nickname
        
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
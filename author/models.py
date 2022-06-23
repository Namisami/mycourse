from django.db import models
from pkg_resources import require

class Author(models.Model):
    nickname = models.CharField(verbose_name="Никнейм", max_length=255)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255, blank=True)

    def __str__(self):
        return self.nickname
        
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
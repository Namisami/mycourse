from django.db import models
from picture.models import Picture
from authentication.models import User

class Album(models.Model):
    title = models.CharField(verbose_name="Название", max_length=255, default="Новый альбом")
    description = models.TextField(verbose_name="Описание", blank=True)
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    cover = models.ImageField(verbose_name="Обложка", upload_to="albums/covers", default="../static/images/placeholder.webp")
    picture = models.ManyToManyField(verbose_name="Изображения", to=Picture, blank=True)
    owner = models.ForeignKey(to=User, verbose_name="Владелец", on_delete=models.CASCADE)

    def get_pictures(self):
        return self.picture.objects.all()

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
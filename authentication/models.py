import email
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.urls.base import reverse

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", unique=True)

    USERNAME_FIELD = 'email'
    # def get_absolute_url(self):
    #     return reverse('model-detail-view', args=[str(self.id)])
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)

    photo = models.ImageField(upload_to='usersprof', blank=True)

    def __str__(self):
        return f'Perfil do usuário {self,user.username}'

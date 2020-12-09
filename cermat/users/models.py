from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class User(AbstractUser):

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(
        "Nome de usuário", blank=True, max_length=255
    )
    photo = models.ImageField("Foto de perfil", upload_to='usersphotos', blank=True)
    researchgate = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    lattes = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )

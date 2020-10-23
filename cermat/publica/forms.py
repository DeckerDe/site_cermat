from .models import Publica
from django.forms import ModelForm


class CreatePublicaForm(ModelForm):
    class Meta:
        model = Publica
        fields = ['title', 'proj','slug', 'author', 'sec_author', 'body', 'status']
        labels = {
            'title': 'Título',
            'proj': 'Projeto',
            'author': 'Primeiro Autor',
            'sec_author': 'Autores secundários',
            'body': 'Descrição',
        }

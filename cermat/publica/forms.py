from .models import Publica
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class CreatePublicaForm(ModelForm):

    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')
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

        help_texts = {
            'slug': 'Preencher da seguinte maneira: Titulo: Meu titulo, Slug: meu-titulo'
        }

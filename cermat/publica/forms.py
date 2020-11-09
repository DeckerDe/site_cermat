from .models import Publica, Author, Organization
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class CreatePublicaForm(ModelForm):

    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')
    class Meta:
        model = Publica
        fields = ['title', 'proj','journal','url', 'body', 'status']
        labels = {
            'title': 'Título',
            'proj': 'Projeto',
            'journal':'journal',
            'url':'Url',
            'body': 'Descrição',
        }

class UpdatePublicaForm(ModelForm):

    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')
    class Meta:
        model = Publica
        fields = ['proj','journal','url', 'body', 'status']
        labels = {
            'proj': 'Projeto',
            'journal':'journal',
            'url':'Url',
            'body': 'Descrição',
        }

class CreateAuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = {'name', 'organization', 'researchgate', 'linkedin', 'lattes'}
        labels = {
            'name': 'Nome',
            'organization': 'Organização',
            'researchgate': 'Researchgate',
            'linkedin': 'Linkedin',
            'lattes': 'Lattes'
        }
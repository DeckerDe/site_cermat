from .models import Publica, Researcher, Organization
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class CreatePublicaForm(ModelForm):

    researchers = forms.ModelChoiceField(queryset=Researcher.objects.all(), required=True)
    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')
    class Meta:
        model = Publica
        fields = ['title', 'proj','journal','url', 'body', 'status','researchers',]
        labels = {
            'title': 'Título',
            'researchers': 'Pesquisadores',
            'proj': 'Projeto',
            'journal':'Journal',
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

class CreateResearcherForm(ModelForm):
    class Meta:
        model = Researcher
        fields = {'name', 'organization', 'researchgate', 'linkedin', 'lattes'}
        labels = {
            'name': 'Nome',
            'organization': 'Organização',
            'researchgate': 'Researchgate',
            'linkedin': 'Linkedin',
            'lattes': 'Lattes'
        }

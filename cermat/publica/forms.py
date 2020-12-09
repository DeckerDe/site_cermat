from .models import Publica, Researcher
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class CreatePublicaForm(ModelForm):
    # researchers = forms.MultipleChoiceField(choices=Researcher.objects.filter())
    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')

    class Meta:
        model = Publica
        fields = ['title', 'proj', 'journal', 'url', 'body', 'status', 'researchers']
        labels = {
            'title': 'Título',
            'proj': 'Projeto',
            'journal': 'Journal',
            'url': 'Url',
            'body': 'Descrição',
            'researchers': 'Pesquisadores',
        }


class UpdatePublicaForm(ModelForm):

    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')

    class Meta:
        model = Publica
        fields = ['proj', 'journal', 'url', 'body', 'status']
        labels = {
            'proj': 'Projeto',
            'journal': 'journal',
            'url': 'Url',
            'body': 'Descrição',
        }


class CreateResearcherForm(ModelForm):
    class Meta:
        model = Researcher
        fields = ['name', 'organization', 'organization_abre', 'researchgate', 'linkedin', 'lattes']
        labels = {
            'name': 'Nome',
            'organization': 'Organização',
            'organization_abre': 'Sigla da organização',
            'researchgate': 'Researchgate',
            'linkedin': 'Linkedin',
            'lattes': 'Lattes'
        }

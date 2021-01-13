from .models import Publica, Researcher
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class CreatePublicaForm(ModelForm):
    body = forms.CharField(widget=SummernoteWidget(), label='Corpo da publicação')

    class Meta:
        model = Publica
        fields = ['title', 'proj', 'journal', 'url', 'abstract', 'graphical_abstract', 'body', 'status', 'researchers']
        labels = {
            'title': 'Título',
            'proj': 'Projeto',
            'journal': 'Journal',
            'abstract': 'Resumo',
            'graphical_abstract': 'Graphical abstract',
            'url': 'Url',
            'body': 'Corpo da publicação',
            'researchers': 'Pesquisadores',
        }
        help_texts = {
            'graphical_abstract': "O GAb tem precedência sobre o resumo, portanto caso for inserido "
                                  "anulará a apresentação deste na lista de publicações. Porém, ele ainda "
                                  "será inserido nos detalhes da publicação.",
            'researchers': "Para selecionar mais de um autor mantenha a tecla CTRL pressionada e clique nos"
                           "respectivos nomes."
        }


class UpdatePublicaForm(ModelForm):

    body = forms.CharField(widget=SummernoteWidget(), label='Descrição')

    class Meta:
        model = Publica
        fields = ['proj', 'journal', 'url', 'abstract', 'graphical_abstract', 'body', 'status', 'researchers']
        labels = {
            'proj': 'Projeto',
            'journal': 'Journal',
            'abstract': 'Resumo',
            'graphical_abstract': 'Graphical abstract',
            'url': 'Url',
            'body': 'Corpo da publicação',
            'researchers': 'Pesquisadores',
        }
        help_texts = {
            'graphical_abstract': "O GAb tem precedência sobre o resumo, portanto caso for inserido "
                                  "anulará a apresentação deste na lista de publicações. Porém, ele ainda "
                                  "será inserido nos detalhes da publicação.",
            'researchers': "Para selecionar mais de um autor mantenha a tecla CTRL pressionada e clique nos"
                           "respectivos nomes."
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

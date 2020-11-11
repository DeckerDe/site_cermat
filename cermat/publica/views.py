from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Publica, Project, Researcher
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import CreatePublicaForm, UpdatePublicaForm, CreateResearcherForm
from django.core import serializers
from django.views.generic.edit import (
    CreateView,
    UpdateView
)
import pdb

def post_list(request):
    query =  request.GET.get('busca')
    if query:
        object_list = Publica.published.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        object_list = Publica.published.all()
    paginator = Paginator(object_list, 5) # 3 Posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the fist page.
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'publica/list.html', {'page':page, 'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Publica, slug=post,
        status = 'publicado',
        publish__year = year,
        publish__month=month,
        publish__day=day)
    return render(request, 'publica/detail.html', {'post':post})

class CreatePublica(LoginRequiredMixin,CreateView):
    template_name_suffix  = '_create_form'
    model = Publica
    form_class = CreatePublicaForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        created = self.request.POST.get('created')
        status = self.request.POST.get('status')
        if status == "rascunho":
            return reverse('users:detail', args=[self.request.user.username])
        else:
            return self.object.get_absolute_url()


class UpdatePublica(LoginRequiredMixin, UpdateView):
    template_name_suffix  = '_create_form'
    model = Publica
    form_class = UpdatePublicaForm

def delete_publica(request, publica_id=None):
    publica_to_delete = Publica.objects.get(id=publica_id)
    publica_to_delete.delete()
    return redirect('users:detail', username=request.user.username)

def lista_projetos(request):
    query =  request.GET.get('busca')
    if query:
        object_list = Projects.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        object_list = Project.objects.all()
    paginator = Paginator(object_list, 5) # 3 Posts in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the fist page.
        projects = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)
    return render(request, 'publica/project_list.html', {'page':page, 'projects':projects})

def projeto_detalhe(request, year, month, day, project_slug):
    project = get_object_or_404(
        Project, slug=project_slug,
        start__year = year,
        start__month = month,
        start__day = day
    )
    return render(request, 'publica/project_detail.html', {'project': project})

def prod_cient(request):
    projects = Project.objects.all().order_by('-start')[:10]

    return render(request, 'publica/scientific.html', { 'projects': projects })



def manage_researcher(request):
    context = {}

    researchers = Researcher.objects.all()

    form = CreateResearcherForm

    context['form'] = form
    context['researchers'] = researchers
    return render(request, "publica/manage_researchers.html", context)





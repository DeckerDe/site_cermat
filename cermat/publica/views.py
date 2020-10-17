from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity
def post_list(request):
    query =  request.GET.get('busca')
    if query:
        object_list = Post.published.filter(Q(title__icontains=query) | Q(body__icontains=query))
    else:
        object_list = Post.published.all()
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
        Post, slug=post,
        status = 'publicado',
        publish__year = year,
        publish__month=month,
        publish__day=day)
    return render(request, 'publica/detail.html', {'post':post})

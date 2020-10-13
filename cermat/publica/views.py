from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):
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

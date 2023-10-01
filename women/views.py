from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *

menu = [{'title': "About us", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Contact us", 'url_name': 'contact'},
        {'title': "log in", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})


def add_page(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = AddPostForm()

    context = {
        'menu': menu,
        'title': 'Add article',
        "form": form
    }

    return render(request, 'women/add_page.html', context)


def contact(request):
    return HttpResponse("<h1>Contact us</h1>")


def login(request):
    return HttpResponse("<h1>Authorization</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_slug):
    cat = get_object_or_404(Category, slug=cat_slug)
    posts = Women.objects.filter(cat_id=cat.pk)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'View category',
        'cat_selected': cat.pk,
    }

    return render(request, 'women/index.html', context=context)

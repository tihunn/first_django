from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

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
    return HttpResponse("Add article")


def contact(request):
    return HttpResponse("<h1>Contact us</h1>")


def login(request):
    return HttpResponse("<h1>Authorization</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Views post with id = {post_id}")


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'View category',
        'cat_selected': cat_id,
    }

    return render(request, 'women/index.html', context=context)

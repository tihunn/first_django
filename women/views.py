from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import *
from .models import *

menu = [{'title': "About us", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Contact us", 'url_name': 'contact'},
        {'title': "log in", 'url_name': 'login'}
        ]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['menu'] = menu
        context['title'] = "Main page"
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Add article"
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse("<h1>Contact us</h1>")


def login(request):
    return HttpResponse("<h1>Authorization</h1>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        context['cat_selected'] = context['post'].cat_id
        return context


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context

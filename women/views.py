from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404

from women.models import Women

menu = ["About site, Add article", "Contact us", "Log in"]


# Create your views here.
def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {"title": "Main page", "menu": menu, "posts": posts})


def about(request):
    return render(request, 'women/about.html', {"title": "About site", "menu": menu})


def categories(request, catid):
    return HttpResponse(f"<h1>Catalog page</h1><p>{catid}</p>")


def archive(request, year):
    if 1970 < int(year) > 2023:
        raise Http404()
    return HttpResponse(f"<h1>Archive for year</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound(f"<h1>Page not found (error 404)</p>")
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {"projects": "Home Page Content"}
    return render(request, "index.html", context)

def blog(request):
    context = {"projects": "Blog Page Content"}
    return render(request, "index.html", context)

def blog_detail(request, id):
    return HttpResponse('Ini Adalah artikel - '+id)

def about(request):
    context = {"projects": "About Page Content"}
    return render(request, "index.html", context)
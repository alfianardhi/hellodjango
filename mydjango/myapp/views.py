from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Ini Home Page</h1>')

def about(request):
    return  HttpResponse('<h1>Ini About Page</h1>')
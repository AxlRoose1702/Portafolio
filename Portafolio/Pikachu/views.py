from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home.html")

def descargacv(request):
    return render(request, "descargarcv.html")

def exp(request):
    return render(request, "experiencia.html")

def about(request):
    return render(request, "about.html")

def project(request):
    return render(request, "proyectos.html")
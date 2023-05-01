from django.shortcuts import render

# Create your views here.
def home(request):
    #projects = Project.objects.all()
    return render(request, "home.html")
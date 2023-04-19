#se agregan las vistas
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="inicio"),
    path('donwload', views.descargacv, name="descargarcv"),
    path('exp', views.exp, name="exp"),
    path('about', views.about, name="about"),
    path('project', views.project, name="proyectos"),
    
]
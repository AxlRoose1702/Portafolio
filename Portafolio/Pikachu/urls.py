#se agregan las vistas
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="inicio"),
    
]
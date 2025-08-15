from django.urls import path
from . import views  #el punto hace referencia a la carpeta padre
urlpatterns = [
    path('', views.index, name='index'),  
]
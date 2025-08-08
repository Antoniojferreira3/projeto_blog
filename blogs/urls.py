# recipes/urls.py
from django.urls import path # Importa a função 'path' que define URLs.
from . import views # Importa o arquivo views.py do próprio app.

urlpatterns = [
path('', views.blog_list, name='blog_list'), # nova view para listar
]
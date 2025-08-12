# recipes/urls.py
#from django.urls import path # Importa a função 'path' que define URLs.
#from . import views # Importa o arquivo views.py do próprio app.

#urlpatterns = [
#path('', views.blog_list, name='blog_list'), # nova view para listar
#]
# blogs/urls.py
from django.urls import path
from . import views

app_name = 'blogs'  # Para usar namespacing nas URLs

urlpatterns = [
    path('', views.blog_list, name='blog_list'),            # Lista todos os blogs
    path('<int:pk>/', views.blog_detail, name='blog_detail') # Detalhe de um blog específico
]
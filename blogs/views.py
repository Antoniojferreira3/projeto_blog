# blogs/views.py
#from django.shortcuts import render, get_object_or_404

#from .models import blog

#def blog_list(request):
  #blogs = blog.objects.all()
  #return render(request, 'blogs/blog_list.html', {'blogs': blogs})
#def blog_detail(request, pk):
  #blog = get_object_or_404(blog, pk=pk)
  #return render(request, 'blogs/blog_detail.html', {'blog': blog})
# blogs/views.py
from django.shortcuts import render, get_object_or_404
from .models import Blog  # Certifique-se que no models está "class Blog(models.Model):"

def blog_list(request):
    """
    Exibe a lista de todos os blogs.
    """
    blogs = Blog.objects.all()
    return render(request, 'blogs/blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    """
    Exibe os detalhes de um Blog específico.
    """
    blog_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blogs/blog_detail.html', {'blog': blog_post})
from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
# Create your views here.

class BlogListView(ListView):
    template_name = 'blog/blogs.html'
    model = Blog

def index(request):
    return render(request, 'blog/blogs.html')

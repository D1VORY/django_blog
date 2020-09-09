from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class BlogListView(ListView):
    template_name = 'blog/blogs.html'
    model = Blog


    def get_queryset(self):
        blogs = Blog.objects.all().order_by('-created')
        return blogs


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog




def index(request):
    return render(request, 'blog/blogs.html')

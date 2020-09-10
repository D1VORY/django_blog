from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView

from .models import Blog
from .forms import BlogForm
# Create your views here.

class BlogListView(ListView):
    template_name = 'blog/blogs.html'
    model = Blog
    paginate_by = 9

    def get_queryset(self):
        blogs = Blog.objects.all().order_by('-created')
        return blogs


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog



class CreateBlogView(FormView):
    template_name = 'blog/create_blog.html'
    form_class = BlogForm
    success_url = './'

    def form_valid(self, form):
        #import pdb; pdb.set_trace()
        if form.is_valid:
            blog = Blog(**form.cleaned_data, author=self.request.user)
            blog.save()
        return super(CreateBlogView, self).form_valid(form)

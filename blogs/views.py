from django.shortcuts import render
from django.views.generic import CreateView
from .models import Blogs
from .forms import BlogForm

# Create your views here.
class AddBlog(CreateView):
    model = Blogs
    form_class = BlogForm
    template_name = "add_blog.html"

from django.shortcuts import render
from .models import Blogs
from django.views.generic import CreateView

# Create your views here.
class CreatePost(CreateView):
    model = Blogs
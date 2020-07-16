from django.shortcuts import render
from django.views.generic import ListView,DeleteView
from . models import Post

class BlogListView(ListView):
    model  = Post
    template_name = 'blog/home.html'

class BlogDetailView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'custom'
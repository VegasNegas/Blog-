from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView
from django.views.generic.edit import CreateView
from . models import Post

class BlogListView(ListView):
    model  = Post
    template_name = 'blog/home.html'

class BlogDetailView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'
    #context_object_name = 'custom'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('autor','titulo','conteudo','status')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('titulo','conteudo')
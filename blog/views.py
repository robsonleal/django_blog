from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('author', 'title', 'content')


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title', 'content')
    context_object_name = 'post'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

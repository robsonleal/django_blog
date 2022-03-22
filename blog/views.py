from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
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


class BlogCreateView(SuccessMessageMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ('author', 'title', 'content')
    success_url = reverse_lazy('home')
    success_message = '"%(title)s" criado com sucesso!'


class BlogUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('title', 'content')
    context_object_name = 'post'
    success_message = '"%(title)s" alterado com sucesso!'


class BlogDeleteView(SuccessMessageMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = '"%(calculated_field)s" deletado com sucesso!'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )

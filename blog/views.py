from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from . import forms
# Create your views here.


class Publish(ListView):
    model = models.Post
    template_name = 'publish.html'
    ordering = ['-id']


class Home(ListView):
    model = models.Post
    template_name = 'home.html'
    ordering = ['id']


class Preview(DetailView):
    model = models.Post
    template_name = 'preview.html'


class AddPost(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'author', 'content')


class UpdatePost(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'update_post.html'


class DeletePost(DeleteView):
    model = models.Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

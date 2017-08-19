from django.shortcuts import render
from django.views.generic import CreateView,ListView,DeleteView, DetailView,UpdateView
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy
# Create your views here.



class PostCreate(CreateView):
    model = Post
    form_class = PostForm


class PostDetail(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_form_update'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')






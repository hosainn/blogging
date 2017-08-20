from django.shortcuts import render
from django.views.generic import (CreateView,ListView,ArchiveIndexView,
                                  DeleteView, DetailView,UpdateView,YearArchiveView,MonthArchiveView)
from .models import Post
from .forms import PostForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm


class PostDetail(DetailView):
    model = Post

class PostList(ArchiveIndexView):
    allow_empty = True
    #allow_future = True
    date_field = 'pub_date'
    model = Post
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'


class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name_suffix = '_form_update'


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_post_list')






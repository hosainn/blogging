from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView
from .models import Tag,Department,NewsLink
from .forms import TagForm
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm

class TagDetail(DetailView):
    model = Tag

class TagList(ListView):
    model = Tag

class TagUpdate(UpdateView):
    model = Tag
    form_class = TagForm
    template_name_suffix = '_form_update'

class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer_tag_list')


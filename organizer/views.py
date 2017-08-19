from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView
from .models import Tag,Department,NewsLink
from .forms import TagForm,DepartmentForm,NewsLinkForm
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


class DepartmentCreate(CreateView):
    model = Department
    form_class = DepartmentForm

class DepartmentList(ListView):
    model = Department


class DepartmentDetail(DetailView):
    model = Department


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('organizer_department_list')

class DepartmentUpdate(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name_suffix = '_form_update'


class NewsLinkCreate(CreateView):
    model = NewsLink
    form_class = NewsLinkForm




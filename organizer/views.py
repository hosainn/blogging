from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView,DeleteView,UpdateView
from .models import Tag,Department,NewsLink
from .forms import TagForm,DepartmentForm,NewsLinkForm
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm

class TagDetail(DetailView):
    model = Tag

class TagList(ListView):
    paginate_by = 3
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
    paginate_by = 3
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


class NewsLinkDelete(DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.department.get_absolute_url())

class NewsLinkUpdate(UpdateView):
    model = NewsLink
    form_class = NewsLinkForm
    slug_url_kwarg = 'newslink_slug'
    template_name_suffix = '_form_update'






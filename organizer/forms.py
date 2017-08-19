from django.core.exceptions import ValidationError
from django import forms
from organizer.models import Department,Tag,NewsLink

class SlugClenMixin:
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "create".')
        return new_slug


class TagForm(SlugClenMixin,forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()


class DepartmentForm(SlugClenMixin,forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class NewsLinkForm(SlugClenMixin,forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'


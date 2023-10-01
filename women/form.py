from django import forms
from .models import *


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=225, label="Title", widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="Part URL")
    content = forms.CharField(widget=forms.Textarea(attrs={"cols": 60, "rows": 10}), label="Content")
    is_published = forms.BooleanField(label="Publish", initial=True, required=False)
    cat = forms.ModelChoiceField(Category.objects.all(), label="Category", empty_label="Category not choice")

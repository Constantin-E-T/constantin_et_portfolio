# constantin_et/blog/forms.py

from django import forms
from .models import Blog

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

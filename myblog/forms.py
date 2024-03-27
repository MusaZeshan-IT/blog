from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['post_title', 'post_description']
        labels = {
            'post_title': 'Title',
            'post_description': 'Description'
        }
        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control mb-2', 'maxlength': '30'}),
            'post_description': forms.Textarea(attrs={'class': 'form-control', 'maxlength': '300'})
        }

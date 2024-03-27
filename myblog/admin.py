'''This import is used to import the admin module'''
from django.contrib import admin
from .models import BlogPost

# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    '''This class is used to display my model 'BlogPost' in the admin panel'''
    list_display = ('id', 'post_author', 'post_title', 'post_description')

admin.site.register(BlogPost, BlogPostAdmin)

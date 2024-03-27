'''This import is added to import models from the Django database'''
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.


class BlogPost(models.Model):
    '''This models is created to add data of blog posts to my database'''
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=32)
    post_description = HTMLField(max_length=1500)
    post_slug = AutoSlugField(
        populate_from='post_title', unique=True, null=True, default=None)
    objects = models.Manager()  # Default Manager

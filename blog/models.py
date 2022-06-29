""""
Instructions for functionality of blog
"""
from django.db import models
from django.contrib.auth.models import User

# Keep drafts and published posts separated
STATUS = ((0, 'Draft'), (1, 'Publish'))


class BlogPost(models.Model):
    """"
    For functionality of posts in blog
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

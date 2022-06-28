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
print ('test django')

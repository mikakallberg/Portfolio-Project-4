from django.db import models
from django.contrib.auth.models import User

# Keep drafts and published posts separated
STATUS = ((0, 'Draft'), (1, 'Publish'))


# For functionality of posts in blog
class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)


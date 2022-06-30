""""
Instructions for functionality of blog
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Keep drafts and published posts separated
STATUS = ((0, 'Draft'), (1, 'Published'))


class BlogPost(models.Model):
    """"
    For functionality of posts in blog
    """
    title = models.CharField(
        max_length=200, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts',
        default=id(0))
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    blog_content = models.TextField(default='Start your story here')
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """ Sets the order of posts to most recently created first """
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Handles total number of likes
        """
        return self.likes.count()


class CommentSection(models.Model):
    """ Handles comments """

    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Handles order of published comments, oldest first.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

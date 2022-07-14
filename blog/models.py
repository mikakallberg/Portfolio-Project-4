""""
Instructions for functionality of blog
"""
from django.db import models
from django.urls import reverse
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
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts',
        default=id(0))
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    alt_tag = models.CharField(max_length=100, default='image related to post')
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


class PostImage(models.Model):
    """ Manages the model for uploading multiple images """
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    alt_tag = models.CharField(max_length=100, default='image related to post')

    def __str__(self):
        return self.post.title


class CommentSection(models.Model):
    """ Handles comments """

    post = models.ForeignKey(
        BlogPost,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        max_length=20,
        related_name='comment_author'
        )
    email = models.EmailField()
    body = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Handles order of published comments, oldest first,
        and return comment
        """
        ordering = ['created_on']

    def __str__(self):
        """ Returns comment with name and comment body"""
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """ Returns comment with primary key"""
        return reverse('post_detail', kwargs={'pk': self.pk})

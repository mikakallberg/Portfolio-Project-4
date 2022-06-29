""""
Testing code functionality in models.py
"""
from django.test import TestCase
from .models import BlogPost


class TestModels(TestCase):
    """"
    Testing class BlogPost
    """
    def setUp(self):
        # Setup run before every test method.
        pass

    def test_BlogPost_title_length(self):
        blogpost = BlogPost.objects.create(title='Test Todo Title')
        self.assertEqual(str(blogpost), 'Test Todo Title')


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

    def test_BlogPost_title_characters(self):
        """ Testing if characters inserted in title is a string """
        blogpost = BlogPost.objects.create(title='Test Todo Title')
        self.assertEqual(str(blogpost), 'Test Todo Title')

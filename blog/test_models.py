""""
Testing code functionality in models.py
"""
import unittest
from django.test import TestCase
from .models import BlogPost


class TestModels(unittest.TestCase):
    """"
    Testing class BlogPost
    """

    def test_post(self):
        post = BlogPost.objects.create(name='Test Todo Post')
        self.assertEqual(str(post), 'Test Todo Post')

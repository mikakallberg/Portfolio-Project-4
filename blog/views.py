from django.shortcuts import render
from django.views import generic
from .models import BlogPost


class PostList(generic.ListView):
    """ Settings for front view of blog """
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

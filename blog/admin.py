""" Admin page for settings in admin view """
from django.contrib import admin
from .models import BlogPost
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """ Handle use of summernote functionality in blog """
    summernote_fields = ('blog_content')

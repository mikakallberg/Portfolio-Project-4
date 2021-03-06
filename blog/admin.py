""" Admin page for settings in admin view """
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import PostImage, BlogPost, CommentSection


class PostImage(admin.StackedInline):
    """ Stacks multiple image upload fields inline """
    model = PostImage


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    """ Handle functionality of blog in admin view """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    inlines = [PostImage]


@admin.register(CommentSection)
class CommentAdmin(admin.ModelAdmin):
    """ Handle comments by Site_Users """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """ Approving comments before publishing """
        queryset.update(approved=True)

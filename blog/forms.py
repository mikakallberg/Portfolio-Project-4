from django import forms
from django.views.generic.edit import CreateView
from .models import CommentSection, BlogPost


class CreatePostForm(CreateView):
    model = BlogPost
    template_name = 'create_post.html'
    fields = ('__all__')
    success_url = '/'


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ('body',)

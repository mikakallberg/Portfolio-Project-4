from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import CommentSection, BlogPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('__all__')
        widgets = {
            'content': SummernoteWidget()
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ('body',)

from .models import CommentSection
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentSection
        fields = ('body',)

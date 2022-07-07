""" Creating in UI view """
from django import forms
from .models import CommentSection


class CommentForm(forms.ModelForm):
    """ Creating a comment in UI """
    class Meta:
        """ Settings for comment in UI """
        model = CommentSection
        fields = ('body',)

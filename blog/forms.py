""" Creating in UI view """
from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CommentSection


class CommentForm(forms.ModelForm):
    """ Creating a comment in UI """
    class Meta:
        """ Settings for comment in UI """
        model = CommentSection
        fields = ('body')
        labels = {
            'body': _('Comment'),
        }

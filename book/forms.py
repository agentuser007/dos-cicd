"""
This module defines the forms used to interact with the Book model.
"""
from django import forms
from .models import Book
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    """
    A form for creating or updating a Book instance.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'publication_date', 'pages']

        """
        Validate the author field.
        """
    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author.startswith(' ') or author.endswith(' '):
            raise ValidationError("Author cannot start or end with a space")
        if '~' in author:
            raise ValidationError("Author cannot contain the '~' character")
        return author.strip()

        """
        Validate the publisher field.
        """
    def clean_publisher(self):
        publisher = self.cleaned_data.get('publisher')
        if publisher.startswith(' ') or publisher.endswith(' '):
            raise ValidationError("Publisher cannot start or end with a space")
        if '~' in publisher:
            raise ValidationError("Publisher cannot contain the '~' character")
        return publisher.strip()
        
        
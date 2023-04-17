"""Module docstring for book models."""
from django.db import models

class Book(models.Model):
    """Book model."""
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publication_date = models.DateField()
    pages = models.IntegerField()

    def __str__(self):
        """Return string representation of book."""
        return str(self.title)

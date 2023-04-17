"""
This module defines the admin interface for the Book model.
"""

from django.contrib import admin
from .models import Book

admin.site.register(Book)

from django.db import models
from django.contrib import admin

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50, null=True)
    author = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return Book.title
    

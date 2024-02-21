from django.db import models
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    objects = None
    book_name = models.CharField(max_length=150)
    book_file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.book_name


class Video(models.Model):
    objects = None
    name = models.CharField(max_length=150)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone

from users.models import MyUser


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


class QuizAttempt(models.Model):
    objects = None
    user = models.ForeignKey(MyUser, on_delete=models.PROTECT)
    score = models.IntegerField()
    date_attempted = models.DateTimeField(auto_now_add=True)


class Quiz(models.Model):
    objects = None
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=20)
    option2 = models.CharField(max_length=20)
    option3 = models.CharField(max_length=20)
    option4 = models.CharField(max_length=20)
    answer = models.CharField(max_length=20)

    def __str__(self):
        return self.question

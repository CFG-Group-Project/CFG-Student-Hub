from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=10000)
    link = models.URLField(max_length=250, blank=True)
    resolved = models.BooleanField(editable=True, default=False)

    class Meta:
        verbose_name = "Student note"
        verbose_name_plural = "Student notes"

    def __str__(self):
        return self.title


class Program(models.Model):
    pathway = models.CharField(max_length=50, primary_key=True)
    path_name = models.CharField(max_length=70)

    def __str__(self):
        return self.path_name


class Material(models.Model):
    lesson = models.CharField(max_length=50, null=True)
    week = models.IntegerField()
    slides = models.CharField(max_length=400)
    code_file = models.CharField(max_length=400, null=True, blank=True)
    show = models.BooleanField(null=True)
    topics = models.CharField(max_length=50, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    sub_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rectutorial = models.URLField(max_length=200, unique=True, null=True, blank=True)

    def __str__(self):
        return self.lesson

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_DEFAULT,default='CFG Grad')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    link = models.URLField(max_length=250, blank=True)

    class Meta:
        verbose_name = "Student Submission"
        verbose_name_plural = "Student Submissions"

    def __str__(self):
        return self.title


class Program(models.Model):
    pathway = models.CharField(max_length=50)
    path_code = models.CharField(max_length=4, primary_key=True)

    def __str__(self):
        return self.pathway


class Topic(models.Model):
    prog = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Material(models.Model):
    lesson = models.CharField(max_length=50,null=True)
    week = models.CharField(max_length=3)
    slides = models.CharField(max_length=400)
    code_file = models.FileField(upload_to='resources/code', null=True)
    show = models.BooleanField(null=True)
    topics = models.CharField(max_length=50, null=True)
    pathway = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    sub_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rectutorial = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.lesson



# class AdminDash(models.Model):


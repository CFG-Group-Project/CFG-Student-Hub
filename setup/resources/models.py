from django.db import models

# Create your models here.

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
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    week = models.CharField(max_length=3)
    slides = models.FileField(upload_to='slides')
    show = models.BooleanField(null=True)
    rectutorial = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.lesson


Topic_Choice = (
    ()
)
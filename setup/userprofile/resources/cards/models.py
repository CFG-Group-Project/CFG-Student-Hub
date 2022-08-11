from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ..models import Program


# Create your models here.
class Topics(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('card-list')


class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    topic = models.ManyToManyField(Topics)
    # program = models.OneToOneField(Program,on_delete=models.CASCADE)

    def __str__(self):
        return self.question

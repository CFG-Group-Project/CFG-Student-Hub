from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    # topic = models.ForeignKey(Topics,default='',on_delete=models.SET_DEFAULT,null=True)
    topic = models.ManyToManyField(Topics)
    def __str__(self):
        return self.question
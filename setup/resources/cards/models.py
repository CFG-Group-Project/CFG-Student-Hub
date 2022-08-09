from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.question
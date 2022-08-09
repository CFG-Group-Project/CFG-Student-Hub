from django.db import models
from ..models import Program
from django.contrib.auth.models import User


# Create your models here.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)

class GlossaryCards(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    box = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    def move(self, solved):
        new_box = self.box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            self.box = new_box
            self.save()

        return self
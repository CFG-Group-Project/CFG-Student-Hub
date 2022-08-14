from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    subbed = models.DateTimeField(auto_now=True)
    resolved = models.BooleanField(editable=True,default=False)

    class Meta:
        verbose_name = "Contact Sub"
        verbose_name_plural = "Contact Subs"

    def __str__(self):
        return str(self.subject) + ' (' + str(self.user) +')'
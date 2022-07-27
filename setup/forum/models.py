from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


# Create your models here.



class Post(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post_id = models.AutoField
    post_content = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(default=now)



class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(default=now)

from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from .resources.models import Program

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

#the use of the Profile model means users need to have completed their profile setup before they can post on the forum
class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="static/avatars/", null=True, blank=True, default="default.jpg")
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    stream = models.ForeignKey(Program,null=True,default='Foundation',on_delete=models.SET_DEFAULT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"


    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = HTMLField()
    date = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # update the view count
    def update_views(self, *args, **kwargs):
        self.views  =+ 1
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'posts'


class Comment(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.CASCADE, default=None)
    likes = models.ManyToManyField(Profile, default=None, blank=True, related_name='likes')
    created_on = models.DateField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')

    def __str__(self):
        return f" {self.user} says '{self.content[:20]}...'"

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False




class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     LIKE_CHOICES = (
#         ('Like', 'Like'),
#         ('unlike', 'unlike'),
#     )
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     value = models.CharField(LIKE_CHOICES,default='Like', max_length=10)
#
#     def __str__(self):
#         return str(self.post)


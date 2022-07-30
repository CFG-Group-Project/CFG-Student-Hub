from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.timezone import now
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount



# Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE())
    username = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    profile_pic = models.ImageField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=400, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

        class Meta:
            verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_id = models.AutoField
    post_content = HTMLField()
    timestamp = models.DateTimeField(default=now)
    categories = models.ManyToManyField(Category)
    date = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    reply_id = models.AutoField
    reply_content = models.CharField(max_length=5000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(default=now)

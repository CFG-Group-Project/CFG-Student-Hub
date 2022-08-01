from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="static/avatars/", null=True, blank=True, default="default.jpg")
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')


class Category(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'


class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    timestamp = models.DateTimeField(default=now)
    date = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'

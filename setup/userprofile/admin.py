from django.contrib import admin

from .models import Profile, Category, Post, Comment, Reply, Like

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)



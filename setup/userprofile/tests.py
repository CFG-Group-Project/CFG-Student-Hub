from django.test import TestCase
from django.contrib.auth.models import AnonymousUser
from .models import Post, Comment, Profile


# Create your tests here.


class DiscussionTests(TestCase):
    def setUp(self):
        self._create_users()

    def _create_users(self):
        self.lisa = Profile.objects.create_user(
            username="lisa", password="top_secret")
        self.sarah = Profile.objects.create_user(
            username="sarah", password="top_secret")
        self.sweetie = Profile.objects.create_user(
            username="sweetie", password="top_secret")
        self.alicia = AnonymousUser()

    def new_discussion(self, user, title):
        """Users can create discussion posts"""
        post = Post(title=title,
                    content="Just testing :)",
                    author=user)
        post.save()
        return post

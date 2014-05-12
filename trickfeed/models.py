from django.db import models
from django.contrib.auth.models import User


class Tricker(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_url = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    author_url = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s".format(self.title, self.youtube_url)
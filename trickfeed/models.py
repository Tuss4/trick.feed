from django.db import models
from django.contrib.auth.models import User


class Tricker(models.Model):
    user = models.OneToOneField(User)
    favorites = models.ManyToManyField('Video')

    def __unicode__(self):
        return self.user.username


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_id = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    author_id = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now=False, auto_now_add=True)
    thumbnail = models.CharField(max_length=100)
    is_tricking = models.NullBooleanField(default=True)

    def __unicode__(self):
        return "%s - %s" % (self.title, self.youtube_id)

    def youtube_url(self):
        return 'https://youtube.com/embed/{}'.format(self.youtube_id)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('trickfeed.views.view_video', args=[str(self.id)])

    class Meta:
        ordering = ['-added']

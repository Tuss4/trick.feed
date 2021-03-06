from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import utc


class Tricker(models.Model):
    '''The tricker/member class.
    Extends the default User class
    via a OneToOneField.'''

    user = models.OneToOneField(User)
    favorites = models.ManyToManyField('Video')

    # Default string representation for a
    # tricker instance.
    def __unicode__(self):
        return self.user.username

    # Return the tricker's api resource
    def resource_uri(self):
        from .api import TrickerResource
        obj = self
        return TrickerResource().get_resource_uri(obj)


class Video(models.Model):
    '''The video class. Represents the data
    scraped from the YouTube API.'''

    title = models.CharField(max_length=100)
    description = models.TextField()
    youtube_id = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    author_id = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now=False, auto_now_add=True)
    thumbnail = models.CharField(max_length=100)
    is_tricking = models.NullBooleanField(default=True)

    # Default unicode string representation
    # of an instance.
    def __unicode__(self):
        return "%s - %s" % (self.title, self.youtube_id)

    # Returns the youtube embed url.
    def youtube_url(self):
        return 'https://youtube.com/embed/{}'.format(self.youtube_id)

    # Returns the url to view the single video.
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('trickfeed.views.view_video', args=[str(self.id)])

    # Method to detect whether, the video
    # was added within the past 24 hours. Should
    # return true or false.
    def is_this_new(self):
        time_offset = datetime.utcnow().replace(tzinfo=utc) - self.added
        if time_offset.days < 1:
            return True
        else:
            return False

    class Meta:
        ordering = ['-added']

    # Return the tricker's api resource
    def resource_uri(self):
        from .api import VideoResource
        obj = self
        return VideoResource().get_resource_uri(obj)

    # Return a title index for the class
    @classmethod
    def title_index(cls):
        return [t.title for t in cls.objects.all().exclude(is_tricking=False)]

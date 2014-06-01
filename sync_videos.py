import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trickfeed.settings")


from trickfeed.models import Video
print Video.objects.all()

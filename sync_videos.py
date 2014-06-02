import os
import json
import urllib2
import pprint

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trickfeed.settings")


from trickfeed.models import Video
from trickfeed.settings_local import REQUEST_URL
from trickfeed.data import data_request


yt_api_json = data_request(REQUEST_URL, 'tricking')
yt_api_dict = json.loads(yt_api_json)
yt_api_vids = yt_api_dict['items']

pprint.pprint(yt_api_vids)

for video in yt_api_vids:
    try:
        # Check to see if the video is already in the
        # trickfeed database.
        db_video = Video.objects.get(youtube_id=video['id']['videoId'])
        print '{} is already on trick.feed.'.format(db_video.title.encode('utf-8'))
    except Video.DoesNotExist:
        # If the video does not exist
        # add it to the database.
        new_video = Video()
        new_video.title = video['snippet']['title']
        new_video.description = video['snippet']['description']
        new_video.youtube_id = video['id']['videoId']
        new_video.author = video['snippet']['channelTitle']
        new_video.author_id = video['snippet']['channelId']
        new_video.save()
        print '{} has been added to the trick.feed database!'.format(new_video.title.encode('utf-8'))

print 'Sync complete.'

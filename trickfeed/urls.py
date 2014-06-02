from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import (home, view_video)
from tastypie.api import Api
from .api import (TrickerResource, VideoResource)

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(VideoResource())
v1_api.register(TrickerResource())

urlpatterns = patterns('',
    url(r'^$', home),
    # Video url
    url(r'^video/(?P<video_id>\d+)/$', view_video),
    # API Urls
    url(r'^api/', include(v1_api.urls)),

    url(r'^admin/', include(admin.site.urls)),
)

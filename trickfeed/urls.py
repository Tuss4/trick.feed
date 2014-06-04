from django.conf.urls import patterns, include, url

from django.contrib import admin
from .views import (home, view_video,
                    login_view, logout_view,
                    registration_view,)
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
    # Login, logout and register
    url(r'^login/', login_view),
    url(r'^logout/$', logout_view),
    url(r'^register/$', registration_view),
    # Captcha URL
    url(r'^captcha/', include('captcha.urls')),
    # Admin URL
    url(r'^admin/', include(admin.site.urls)),
)

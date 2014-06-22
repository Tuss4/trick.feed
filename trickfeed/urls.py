from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib import admin
from .views import (home, view_video,
                    login_view, logout_view,
                    registration_view,
                    list_favorites,
                    search,)
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
    url(r'^search/', search),
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
    # Member URLs
    url(r'^favorites/$', list_favorites),
    # url(r'^crud_video/(?P<video_id>\d+)/', crud_video)
    # Robots.txt
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain')),
)

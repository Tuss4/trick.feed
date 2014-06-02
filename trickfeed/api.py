from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from models import (Tricker, Video)


class VideoResource(ModelResource):
    class Meta:
        queryset = Video.objects.all()
        resource_name = 'video'
        authorization = Authorization()

    def dehydrate(self, bundle):
        bundle.data['youtube_url'] = bundle.obj.youtube_url()
        return bundle


class TrickerResource(ModelResource):
    favorites = fields.ToManyField('trickfeed.api.VideoResource', 'favorites',
                                   null=True, full=True)

    class Meta:
        queryset = Tricker.objects.all()
        resource_name = 'tricker'
        authorization = Authorization()
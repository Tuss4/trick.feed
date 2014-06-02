from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from .models import Video
# from django.http import HttpResponseRedirect


def home(request):
    return render(request,
                  'home.html',
                  dict(videos=Video.objects.all()),
                  context_instance=RequestContext(request))


def view_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request,
                  'view_video.html',
                  dict(video=video),
                  context_instance=RequestContext(request))

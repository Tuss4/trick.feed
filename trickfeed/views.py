import json


from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import (Video, Tricker)
from .forms import (LoginForm, RegistrationForm)


# Context processor
def videos_context_processor(request):
    return {'videos': Video.objects.all().exclude(is_tricking=False),
            'video_titles': json.dumps(Video.title_index())}


# Home page view.
def home(request):
    videos = Video.objects.all().exclude(is_tricking=False)
    return render(request,
                  'home.html',
                  dict(videos=videos),
                  context_instance=RequestContext(request))


# Single page view for a video.
def view_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request,
                  'view_video.html',
                  dict(video=video),
                  context_instance=RequestContext(request))


# CRUD AJAX for video
# Temporary solution until
# Hydrate M2M override
@csrf_exempt
def crud_video(request, video_id):
    if request.is_ajax():
        if request.method == "PUT":
            try:
                video = Video.objects.get(pk=video_id)
                request.user.tricker.favorites.add(video)
                return HttpResponse("Success",
                                    content_type="application/json")
            except Video.DoesNotExist:
                return HttpResponse("Error, video does not exist",
                                    content_type="application/json")
        if request.method == "DELETE":
            try:
                video = Video.objects.get(pk=video_id)
                request.user.tricker.favorites.remove(video)
                return HttpResponse("Success",
                                    content_type="application/json")
            except Video.DoesNotExist:
                return HttpResponse("Error, video does not exist",
                                    content_type="application/json")


# Display an authenticated user's favorites.
@login_required
def list_favorites(request):
    favorites = request.user.tricker.favorites.all()
    return render(request,
                  'view_favs.html',
                  dict(favorites=favorites),
                  context_instance=RequestContext(request))


# Custom login view.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print 'This account has been disabled.'
            else:
                print 'Invalid login.'
    else:
        form = LoginForm()
    return render(request, 'login.html',
                  dict(form=form),
                  context_instance=RequestContext(request))


# Custom logout view.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# Custom registration view.
def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User()
            new_user.username = username
            new_user.password = password
            new_user.email = email
            new_user.set_password(password)
            new_user.save()
            new_tricker = Tricker()
            new_tricker.user = new_user
            new_tricker.save()
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html',
                  dict(form=form),
                  context_instance=RequestContext(request))


# Video search view.
def search(request):
    results = []
    query_str = ''
    if request.method == 'GET':
        if request.GET.get('video-search'):
            query_str = request.GET.get('video-search')
            results = Video.objects.filter(title__icontains=query_str,
                                           is_tricking=True)
    return render(request, 'search.html',
                  dict(results=results,
                       query=query_str),
                  context_instance=RequestContext(request))

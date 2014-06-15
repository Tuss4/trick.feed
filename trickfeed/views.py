from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import (Video, Tricker)
from .forms import (LoginForm, RegistrationForm)
from .api import (VideoResource, TrickerResource)


# Home page view.
def home(request):
    return render(request,
                  'home.html',
                  dict(videos=Video.objects.all()),
                  context_instance=RequestContext(request))


# Single page view for a video.
def view_video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    # video_res = VideoResource()
    # video_bundle = video_res.build_bundle(obj=video)
    # video_dehydrate = video_res.full_dehydrate(video_bundle, for_list=True)
    # video_json = video_res.serialize(None,
    #                                  video_dehydrate,
    #                                  "application/json")
    return render(request,
                  'view_video.html',
                  dict(video=video),
                  context_instance=RequestContext(request))


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

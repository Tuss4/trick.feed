from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import (Video, Tricker)
from .forms import (LoginForm, RegistrationForm)


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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


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

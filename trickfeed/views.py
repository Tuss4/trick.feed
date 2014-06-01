from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect


def home(request):
    return render(request,
                  'home.html',
                  dict(),
                  context_instance=RequestContext(request))
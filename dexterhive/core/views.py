from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    return render(request, 'index.html')
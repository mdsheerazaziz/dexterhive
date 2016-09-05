from django.http.response import HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    return render(request, 'home.html')


def dash_board(request):
    return render(request, 'dashboard.html')


from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from dexterhive.core.resources import get_user_details


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/dashboard')
    return render(request, 'home.html')


def dash_board(request):
    context = {'user_details': get_user_details(request.user)}
    return render(request, 'dashboard.html', context)


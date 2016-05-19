from os import listdir, path
from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .models import *

def game(request, curr_game):
    # temporary
    active_games = Game.objects.filter(episode__is_active=True).distinct()
    return render(request, 'main/game.html', {'game' : curr_game, 'active_games' : active_games })

def index(request):
    if request.user.is_authenticated(): # temporary
        print User_episode.objects.filter(user=request.user)
        return render(request, 'main/auth.html')
    else:
        return render(request, 'main/index.html')

def tutorial(request):
    return render(request, 'main/tutorial.html')

def rules(request):
    return render(request, 'main/rules.html')


# This might not belong here. But yeah, keep it here at the moment.
def check_auth(request):
    """Instead of using django's admin-interface, redirect to CAS-login if user tries to access
    the admin site while not being authenticated"""
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect('/admin/')
        else:
            return render(request, 'main/index.html')
    else:
        return redirect('/login/')

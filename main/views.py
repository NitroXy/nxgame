# encoding: utf-8
from os import listdir, path
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .models import *
from datetime import timedelta

@login_required
def game(request, curr_game):
    template = 'main/game.html'

    if request.method == "GET":
        active_game = Game.objects.get(name='nxgame21') # Temporary, get this from database later

        active_episodes = Episode.objects.filter(game=active_game, is_active=True)

        if not active_episodes:
            return render(request, template, {'message' : "Nxgame har inte startat yet" })

        for e in active_episodes:
            # Check if episode has started
            headstart = Headstart.objects.get_or_none(user=request.user, episode=e)
            if not e.can_play(headstart.headstart if headstart else 0):
                message = 'Episode %s har inte startat än. Den startar %s.' %\
                        (e.number, e.start_time.strftime("%d %B klockan %H:%M.%S"))
                if headstart:
                    message += " Eftersom du har ett försprång så startar du klockan %s" %\
                            (e.start_time - timedelta(seconds=headstart.headstart)).strftime("%H:%M.%S")
                return render(request, template, {'message' : message})

            # Add initial user-episode-data if user has not played the episode before
            user_episode = User_episode.objects.get_or_none(user=request.user, episode=e)
            if not user_episode:
                user_episode = User_episode(user=request.user, episode=e)
                user_episode.save()

            if not user_episode.finished:
                question = Question.objects.get_or_none(episode=e, number=user_episode.current_question)
                user_question = User_question.objects.get_or_none(user=request.user, question=question)
                if not user_question:
                    user_question = User_question(user=request.user, question=question)
                    user_question.save()
                timehints = Timehint.objects.filter(
                        question=question,
                        delay__lt=(timezone.now() - user_question.start_time).total_seconds())
                return render(request, 'main/game.html',
                        {'game' : curr_game, 'question' : question, 'hints' : timehints })
        # Exiting the for-loop means that the game is completed for that user.
        return render(request, 'main/game.html', {'game' : curr_game, 'message' : "Du har klarat av nxgame! Du kom på plats %s" % user_episode.finish_place()})

    elif request.method == "POST":
        pass

    return render(request, 'main/game.html', {'game' : curr_game, 'active_games' : episodes })

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

def old(request):
    return render(request, 'main/old.html')


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

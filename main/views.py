# encoding: utf-8
from os import listdir, path
from django.template import loader
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .models import *
from datetime import timedelta
from itertools import groupby

@login_required
def game(request):
    game_template = 'main/game.html'

    active_game = Game.objects.get(name='nxgame21') # Temporary, get this from database later
    game_episodes = Episode.objects.filter(game=active_game)

    if not game_episodes:
        messages.add_message(
            request,
            messages.WARNING,
            "Nxgame har inte startat än"
        )
        return render(request, game_template)

    unfinished_episode = User_episode.get_unfinished_episode(request, game_episodes)

    if not unfinished_episode or not unfinished_episode.playable(request):
        return render(request, game_template)

    question = Question.objects.get_or_none(
        episode=unfinished_episode.episode,
        number=unfinished_episode.current_question
    )

    if request.method == "GET":
        user_question, _ = User_question.objects.get_or_create(
            user=request.user,
            question=question,
        )

        hints = Timehint.objects.filter(
            question=question,
            delay__lt=(timezone.now() - user_question.start_time).total_seconds()
        )
        return render(request, game_template, { 'hints' : hints, 'question' : question })

    elif request.method == "POST":
        user_answer = request.POST.get('user-answer')
        correct_answers = Question_answer.get_all_answers(question)
        trigger_replies = Question_reply.get_all_triggers_and_replies(question)

        # TODO, write a handler/view when answer has been given.
        # It should be a view which says which place you finished the question on etc.
        # Right now, just show a message to the next view.
        if user_answer in correct_answers:
            unfinished_episode.make_progress()
            messages.add_message(request, messages.INFO, 'RÄTT')
        elif user_answer in trigger_replies:
            messages.add_message(
                request,
                messages.INFO,
                'TRIGGERED: %s' % trigger_replies[user_answer]
            )
        else:
            messages.add_message(request, messages.INFO, 'FEL')
        return redirect('/game/')

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

def profile(request):
    finished_questions = User_question.objects.filter(user=request.user, finish_time__isnull=False)
    episode_user_groups = {}
    for episode, questions in groupby(finished_questions, lambda x: x.question.episode):
        episode_user_groups[episode] = list(questions)
    return render(request, 'main/profile.html',
            {
                'profile_data' : episode_user_groups,
                'progress_done' : True if finished_questions else False
            })

def old(request):
    return render(request, 'main/old.html')

# This might not belong here. But yeah, keep it here at the moment.
# TODO: Move to middleware.py
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

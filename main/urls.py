from django.conf.urls import url

from . import views
from views import *

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^rules/$', views.rules, name='rules'),
        url(r'^tutorial/$', views.tutorial, name='tutorial'),
	url(r'^game/(?P<curr_game>[0-9]*)/?$', views.game, name='game'),
        url(r'^old/$', views.old, name='old'),
]

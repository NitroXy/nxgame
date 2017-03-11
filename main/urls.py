from django.conf.urls import url
from django.conf.urls.static import static

from . import views
from main.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^tutorial/$', views.tutorial, name='tutorial'),
    url(r'^game/$', views.game, name='game'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^old/$', views.old, name='old'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

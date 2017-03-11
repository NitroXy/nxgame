from __future__ import unicode_literals

from django.apps import AppConfig
from django_cas_ng.signals import cas_user_authenticated
from django.dispatch import receiver


class MainConfig(AppConfig):
    name = 'main'

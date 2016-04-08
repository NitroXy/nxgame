from django_cas_ng.signals import cas_user_authenticated
from django.dispatch import receiver

@receiver(cas_user_authenticated)
def my_handler(*args, **kwargs):
	print args
	print kwargs

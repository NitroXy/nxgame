from os import listdir, path
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
	print request.session.get_expiry_date()
	if request.user.is_authenticated(): # temporary
		return render(request, 'main/auth.html')
	else:
		return render(request, 'main/index.html')

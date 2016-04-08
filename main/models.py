
from django.conf import settings
from django.db import models
class MyUser(models.Model):
	id = models.IntegerField(primary_key=True)  # AutoField?
	password = models.CharField(max_length=128)
	last_login = models.DateTimeField(blank=True, null=True)
	is_HAX = models.BooleanField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=254)
	is_staff = models.BooleanField()
	is_active = models.BooleanField()
	date_joined = models.DateTimeField()
	username = models.CharField(unique=True, max_length=30)

	REQUIRED_FIELDS = ()
	USERNAME_FIELD = 'username'

	class Meta:
		managed = False
		db_table = 'auth_user'

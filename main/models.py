from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, id, username, fullname, **extra_fields):
        """
        Creates and saves a User with the given id, username and fullname
        """
        user = self.model(id=id, username=username, fullname=fullname, **extra_fields)
        user.save(using=self._db)
        return user

    def create_user(self, id, username, fullname, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(id, username, fullname, **extra_fields)

    def create_superuser(self, id, username, fullname, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(id, username, fullname, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
    )
    fullname = models.CharField(_('fullname'), max_length=100)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [id, username, fullname]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

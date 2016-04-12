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

class Game(models.Model):
    name = models.CharField(max_length=128, primary_key=True)

class Episode(models.Model):
    name = models.CharField(max_length=128)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    number = models.IntegerField()

    class Meta:
        unique_together = ('name', 'number')

class User_episode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    current_question = models.IntegerField(default=1)
    finished = models.BooleanField(default=False)
    finish_time = models.DateTimeField(null=True) # Might be redundant to have, since we already will have finish time for each question.

    class Meta:
        unique_together = ('user', 'episode')

class Question(models.Model):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    question = models.CharField(max_length=2048)

    class Meta:
        unique_together = ('episode', 'number')

class Headstart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    headstart = models.IntegerField()

    class Meta:
        unique_together = ('user', 'episode', 'headstart')

class Timehint(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint = models.CharField(max_length=256)
    delay = models.IntegerField()

    class Meta:
        unique_together = ('question', 'delay')

class Finish_time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    finish_time = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'question')

class Question_answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    class Meta:
        unique_together = ('question', 'answer')

class Question_reply(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    trigger = models.CharField(max_length=256)
    reply = models.CharField(max_length=256)

    class Meta:
        unique_together = ('question', 'reply')

class User_answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
    time = models.DateTimeField(default=timezone.now)

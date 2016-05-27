# encoding: utf-8
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta

class BaseManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return []

class BaseModel(models.Model):
    objects = BaseManager()
    class Meta:
        abstract=True

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
        extra_fields.setdefault('is_staff', True)

        return self._create_user(id, username, fullname, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
    )
    fullname = models.CharField(_('fullname'), max_length=100)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now())

    objects = UserManager()

    # Needed by django.contrib.auth
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [id, username, fullname]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Needed by the admin interface
    def get_short_name(self):
        return self.fullname

    def get_full_name(self):
        return self.fullname

class Game(BaseModel):
    name = models.CharField(max_length=128, primary_key=True)

    def __unicode__(self):
        return u'%s' % self.name

class Episode(BaseModel):
    name = models.CharField(max_length=128)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    number = models.IntegerField()
    people = models.ManyToManyField(User, through='User_episode')

    class Meta:
        unique_together = ('name', 'number')
        ordering = ['game', 'number']

    def __unicode__(self):
        return u'%s: %s' % (self.number, self.name)

    def can_play(self, headstart=0):
        headstart = timedelta(seconds=headstart)
        return self.start_time < timezone.now() - headstart < self.end_time

class User_episode(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    current_question = models.IntegerField(default=1)
    finished = models.BooleanField(default=False)
    finish_time = models.DateTimeField(null=True) # Might be redundant to have, since we already will have finish time for each question.

    def finish_place(self):
        betters = User_episode.objects.filter(episode=self.episode, finish_time__lt=self.finish_time)
        return len(betters) + 1

    class Meta:
        unique_together = ('user', 'episode')

    def __unicode__(self):
        return u'User: %s, episode: %s' % (self.user, self.episode)

class Question(BaseModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    question = models.CharField(max_length=2048)
    users = models.ManyToManyField(User, through='User_question')

    class Meta:
        unique_together = ('episode', 'number')
        ordering = ['episode', 'number']

    def __unicode__(self):
        return u'Fråga %s: %s' % (self.number, self.title)

class User_question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now())

    def __unicode__(self):
        return u'User: %s, question: %s' % (self.user, self.question)

class Headstart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    headstart = models.IntegerField()

    class Meta:
        unique_together = ('user', 'episode', 'headstart')

class Timehint(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    hint = models.CharField(max_length=256)
    delay = models.IntegerField()

    class Meta:
        unique_together = ('question', 'delay')

class Finish_time(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    finish_time = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'question')

class Question_answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    class Meta:
        unique_together = ('question', 'answer')

class Question_reply(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    trigger = models.CharField(max_length=256)
    reply = models.CharField(max_length=256)

    class Meta:
        unique_together = ('question', 'reply')

class User_answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
    time = models.DateTimeField(default=timezone.now())

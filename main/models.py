# encoding: utf-8
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta
from .handlers import get_game_upload_folder
from os import path, remove

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
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

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
    is_active = models.BooleanField()

    @transaction.atomic
    def save(self, *args, **kwargs):
        super(Game, self).save(*args, **kwargs)
        if self.is_active:
            active_games = Game.objects.filter(is_active=True).exclude(name=self.name)
            for game in active_games:
                game.is_active = False
                game.save()

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


class User_episode(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    current_question = models.IntegerField(default=1)
    finished = models.BooleanField(default=False)
    finish_time = models.DateTimeField(null=True) # Might be redundant to have,
                                                  # since we already will have finish time for each question.

    def finish_place(self):
        users_ahead = User_episode.objects.filter(episode=self.episode, finish_time__lt=self.finish_time)
        return len(users_ahead) + 1

    def playable(self, request):
        """Checks whether the gives user in the request can play or not."""
        headstart = Headstart.objects.get_or_none(user=request.user, episode=self.episode)
        headstart = timedelta(seconds=headstart.headstart if headstart else 0)

        can_play = self.episode.start_time < timezone.now() + headstart < self.episode.end_time + headstart
        if not can_play:
            messages.add_message(
                request,
                messages.INFO, 'Episode %s har inte startat än. Den startar %s.' %
                    current_episode.number,
                    current_episode.start_time.strftime("%d %B klockan %H:%M.%S"))
            if headstart:
                messages.add_message(
                    request,
                    messages.INFO,
                    "Eftersom du har ett försprång så startar du klockan %s" %
                        (current_episode.start_time - timedelta(seconds=headstart.headstart))
                            .strftime("%H:%M.%S")
                )
        return can_play

    class Meta:
        unique_together = ('user', 'episode')

    @staticmethod
    def get_unfinished_episode(request, episodes):
        for e in episodes:
            candidate, _ = User_episode.objects.get_or_create(user=request.user, episode=e)
            if not candidate.finished:
                return candidate
        # Since the last episode available was finished, nxgame is complete for the user
        messages.add_message(
            request,
            messages.INFO,
            "Du har klarat av nxgame! Du kom på plats %s" % candidate.finish_place()
        )
        return False

    def make_progress(self):
        max_question_number = Question.objects.filter(
            episode=self.episode
            ).aggregate(models.Max('number')).values()[0]
        if self.current_question == max_question_number:
            self.finished = True
            self.finish_time = timezone.now() # Keep redundancy for now
        user_question = User_question.objects.get(
            question=Question.objects.get(episode=self.episode, number=self.current_question),
            user=self.user
        )
        user_question.finish_time = timezone.now()
        user_question.save()
        self.current_question += 1
        self.save()

    def __unicode__(self):
        return u'User: %s, episode: %s' % (self.user, self.episode)

    class Meta:
        unique_together = ('user', 'episode')


class Question(BaseModel):
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    number = models.IntegerField()
    title = models.CharField(max_length=128)
    question = models.TextField(max_length=4096)
    users = models.ManyToManyField(User, through='User_question')

    class Meta:
        unique_together = ('episode', 'number')
        ordering = ['episode', 'number']

    def __unicode__(self):
        return u'Fråga %s: %s' % (self.number, self.title)

class User_question(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    finish_time = models.DateTimeField(null=True)

    @property
    def finish_place(self):
        users_ahead = User_question.objects.filter(question=self.question, finish_time__lt=self.finish_time)
        return len(users_ahead) + 1

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

class Question_answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)

    @staticmethod
    def get_all_answers(question):
        answers = Question_answer.objects.filter(question=question)
        return [x.answer for x in answers]

    class Meta:
        unique_together = ('question', 'answer')

class Question_reply(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    trigger = models.CharField(max_length=256)
    reply = models.CharField(max_length=256)

    @staticmethod
    def get_all_triggers_and_replies(question):
        reply_objects = Question_reply.objects.filter(question=question)
        trigger_replies = {}
        for o in reply_objects:
            trigger_replies[o.trigger] = o.reply
        return trigger_replies

    class Meta:
        unique_together = ('question', 'reply')


class Question_upload(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    upload = models.FileField(upload_to=get_game_upload_folder)

    @staticmethod
    def get_all_uploads(question):
        uploads = Question_upload.objects.filter(question=question)
        return [x.upload for x in uploads]

    class Meta:
        unique_together = ('question', 'upload')

    def save(self, *args, **kwargs):
        # TODO: Validate this in upload form.
        if not path.exists(
                path.join(
                    settings.MEDIA_ROOT,
                    get_game_upload_folder(self, self.upload.name))):
            super(Question_upload, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        remove(self.upload._get_path())
        super(Question_upload, self).delete(*args, **kwargs)

class User_answer(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=256)
    time = models.DateTimeField(default=timezone.now)

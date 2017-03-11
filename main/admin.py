from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'game')
    list_filter = ('game',)


class QuestionAnswerInline(admin.TabularInline):
    model = Question_answer
    extra = 1


class QuestionUploadInline(admin.TabularInline):
    model = Question_upload
    extra = 1


class TimehintInline(admin.TabularInline):
    model = Timehint
    extra = 1


class QuestionReplyInline(admin.TabularInline):
    model = Question_reply
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = ('episode', 'episode__game')
    list_display = ('title', 'get_game', 'episode', 'number')
    inlines = [
        QuestionUploadInline,
        QuestionAnswerInline,
        TimehintInline,
        QuestionReplyInline,
    ]

    def get_game(self, obj):
        return obj.episode.game
    get_game.short_description = 'Game'


@admin.register(Headstart)
class HeadstartAdmin(admin.ModelAdmin):
    list_filter = ('episode__game', 'episode')
    list_display = ('get_game', 'episode', 'user', 'headstart')

    def get_game(self, obj):
        return obj.episode.game
    get_game.short_description = 'Game'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'fullname', 'is_staff', 'date_joined')

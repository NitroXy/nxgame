from django.conf import settings
from os import path
import main.models

def get_game_upload_folder(instance, filename):
    game = models.Episode.objects.get_or_none(name=instance.question.episode.name).game
    return path.join(game.name, filename)

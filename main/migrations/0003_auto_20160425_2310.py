# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 23:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_initial_game_design'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_reply',
            name='trigger',
        ),
        migrations.RemoveField(
            model_name='user_answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='user_answer',
            name='time',
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user_answer',
            name='episode',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.Episode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_answer',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]

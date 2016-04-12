# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 01:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Finish_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('name', models.CharField(max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Headstart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headstart', models.IntegerField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Episode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('title', models.CharField(max_length=128)),
                ('question', models.CharField(max_length=2048)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Episode')),
            ],
        ),
        migrations.CreateModel(
            name='Question_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Question_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(max_length=256)),
                ('reply', models.CharField(max_length=256)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Timehint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint', models.CharField(max_length=256)),
                ('delay', models.IntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
            ],
        ),
        migrations.CreateModel(
            name='User_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_question', models.IntegerField(default=1)),
                ('finished', models.BooleanField(default=False)),
                ('finish_time', models.DateTimeField(null=True)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Episode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='finish_time',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Question'),
        ),
        migrations.AddField(
            model_name='finish_time',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='episode',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Game'),
        ),
        migrations.AlterUniqueTogether(
            name='user_episode',
            unique_together=set([('user', 'episode')]),
        ),
        migrations.AlterUniqueTogether(
            name='timehint',
            unique_together=set([('question', 'delay')]),
        ),
        migrations.AlterUniqueTogether(
            name='question_reply',
            unique_together=set([('question', 'reply')]),
        ),
        migrations.AlterUniqueTogether(
            name='question_answer',
            unique_together=set([('question', 'answer')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('episode', 'number')]),
        ),
        migrations.AlterUniqueTogether(
            name='headstart',
            unique_together=set([('user', 'episode', 'headstart')]),
        ),
        migrations.AlterUniqueTogether(
            name='finish_time',
            unique_together=set([('user', 'question')]),
        ),
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together=set([('name', 'number')]),
        ),
    ]
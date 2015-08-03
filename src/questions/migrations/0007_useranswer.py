# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0006_auto_20150728_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('my_answer_level', models.CharField(max_length=50, choices=[(b'Expert', b'Expert'), (b'Intermediate', b'Intermediate'), (b'Beginner', b'Beginner')])),
                ('tutor_answer_level', models.CharField(max_length=50, choices=[(b'Expert', b'Expert'), (b'Intermediate', b'Intermediate'), (b'Beginner', b'Beginner')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('my_answer', models.ForeignKey(related_name='user_answer', to='questions.Answer')),
                ('question', models.ForeignKey(to='questions.Question')),
                ('tutor_answer', models.ForeignKey(related_name='match_answer', blank=True, to='questions.Answer', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

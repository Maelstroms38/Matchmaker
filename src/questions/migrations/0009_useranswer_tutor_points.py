# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_useranswer_my_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='tutor_points',
            field=models.IntegerField(default=-1),
        ),
    ]

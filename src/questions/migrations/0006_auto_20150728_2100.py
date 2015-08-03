# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20150728_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question',
            new_name='questions',
        ),
    ]

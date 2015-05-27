# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_answer_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='child_number',
            field=models.CharField(default=b'', max_length=9),
        ),
    ]

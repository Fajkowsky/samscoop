# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landingpage', '0002_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
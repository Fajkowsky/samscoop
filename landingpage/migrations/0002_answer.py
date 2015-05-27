# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('yes_no', models.BooleanField()),
                ('ages', models.CharField(max_length=255)),
                ('question_id', models.ForeignKey(to='landingpage.Questions')),
            ],
        ),
    ]

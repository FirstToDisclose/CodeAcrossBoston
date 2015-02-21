# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disclosures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disclosure',
            name='disclosure_text',
        ),
        migrations.AddField(
            model_name='disclosure',
            name='abstract',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='body',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 21, 50, 56, 777564, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='owner',
            field=models.ForeignKey(default=datetime.datetime(2015, 2, 21, 21, 51, 1, 405032, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 21, 21, 51, 14, 42325, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

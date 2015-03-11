# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disclosures', '0002_auto_20150221_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='disclosure',
            name='abstract_file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disclosure',
            name='body_file',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='abstract',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='disclosure',
            name='body',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]

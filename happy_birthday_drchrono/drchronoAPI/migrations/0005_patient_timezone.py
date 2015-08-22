# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0004_auto_20150820_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='timezone',
            field=models.CharField(default=b'UTC', max_length=255),
        ),
    ]

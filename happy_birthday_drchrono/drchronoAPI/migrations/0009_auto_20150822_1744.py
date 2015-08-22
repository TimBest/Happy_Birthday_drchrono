# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timezones', '0001_initial'),
        ('drchronoAPI', '0008_auto_20150822_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='state',
        ),
        migrations.AddField(
            model_name='patient',
            name='us_state',
            field=models.ForeignKey(verbose_name='state', blank=True, to='timezones.State', null=True),
        ),
    ]

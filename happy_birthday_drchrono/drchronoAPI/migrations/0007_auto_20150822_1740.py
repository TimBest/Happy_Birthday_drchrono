# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0006_auto_20150822_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(related_name='patients', verbose_name='state', to='timezones.State'),
        ),
    ]

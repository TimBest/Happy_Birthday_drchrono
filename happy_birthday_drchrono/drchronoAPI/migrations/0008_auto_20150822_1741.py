# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0007_auto_20150822_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(verbose_name='state', to='timezones.State'),
        ),
    ]

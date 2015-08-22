# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0009_auto_20150822_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='us_state',
            new_name='state',
        ),
    ]

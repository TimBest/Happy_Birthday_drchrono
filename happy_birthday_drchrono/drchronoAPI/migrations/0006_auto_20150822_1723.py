# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0005_patient_timezone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(max_length=2),
        ),
    ]

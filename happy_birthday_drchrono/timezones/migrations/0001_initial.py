# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state', models.CharField(max_length=2, unique=True, serialize=False, primary_key=True)),
                ('timezone', models.CharField(default=b'PST', max_length=4)),
            ],
        ),
    ]

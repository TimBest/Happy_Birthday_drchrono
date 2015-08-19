# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.CharField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('doctor', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('cell_phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('state', models.CharField(max_length=255)),
                ('user', models.ForeignKey(related_name='patients', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

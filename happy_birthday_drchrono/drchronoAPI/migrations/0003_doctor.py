# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drchronoAPI', '0002_auto_20150819_0339'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.CharField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('suffix', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('specialty', models.CharField(max_length=255)),
                ('cell_phone', models.CharField(max_length=255)),
                ('home_phone', models.CharField(max_length=255)),
                ('office_phone', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=255)),
                ('user', models.ForeignKey(related_name='doctors', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

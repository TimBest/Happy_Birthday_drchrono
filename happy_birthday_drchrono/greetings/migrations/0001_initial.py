# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappyBirthday',
            fields=[
                ('user', models.OneToOneField(related_name='happy_birthday', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('is_active', models.BooleanField(default=True)),
                ('sms', models.CharField(max_length=160, null=True, verbose_name='text', blank=True)),
                ('email_subject', models.CharField(max_length=77, null=True, verbose_name='subject', blank=True)),
                ('email_body', models.TextField(null=True, verbose_name='body', blank=True)),
            ],
        ),
    ]

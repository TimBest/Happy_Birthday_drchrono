# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0006_auto_20150819_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthday',
            name='sms',
            field=models.CharField(default=b'Happy Birthday', max_length=160, null=True, verbose_name='text', blank=True),
        ),
    ]

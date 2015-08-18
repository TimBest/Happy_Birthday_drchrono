# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0004_auto_20150818_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthday',
            name='notification_type',
            field=models.CharField(default=b'e', max_length=1, verbose_name='notification method', choices=[(b's', 'SMS'), (b'e', 'Email')]),
        ),
    ]

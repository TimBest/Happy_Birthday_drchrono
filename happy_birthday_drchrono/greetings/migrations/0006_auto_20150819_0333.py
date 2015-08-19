# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0005_auto_20150818_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='happybirthday',
            name='last_ran',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='happybirthday',
            name='notification_type',
            field=models.CharField(default=b's', max_length=1, verbose_name='notification method', choices=[(b'e', 'Email'), (b's', 'SMS')]),
        ),
    ]

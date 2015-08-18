# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0003_happybirthday_notification_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthday',
            name='notification_type',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='notification method', choices=[(b's', 'sms'), (b'e', 'Email')]),
        ),
    ]

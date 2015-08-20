# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0009_auto_20150820_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthday',
            name='email_body',
            field=models.TextField(default=b'Hello $patients-first-name,\n\nJust wanted to wish you a Happy $patients-age Birthday!\n\nAll the best,\n\n-   Dr. $doctors-first-name $doctors-last-name $doctors-suffix\n\n$doctors-job-title\nPhone: $doctors-office-phone\nEmail: $doctors-email', null=True, verbose_name='body', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0007_auto_20150820_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='happybirthday',
            name='email_body',
            field=models.TextField(default=b'Hello $patients-first-name,\n                                            Just wanted to wish you a Happy $patients-age Birthday!\n\n                                            All the best,\n\n                                                -   Dr. $doctors-first-name $doctors-last-name $doctors-suffix\n\n                                            $doctors-job-title\n                                            Phone: $doctors-office-phone\n                                            Email: $doctors-email', null=True, verbose_name='body', blank=True),
        ),
        migrations.AlterField(
            model_name='happybirthday',
            name='email_subject',
            field=models.CharField(default=b'Happy Birthday $patients-first-name $patients-last-name!', max_length=77, null=True, verbose_name='subject', blank=True),
        ),
        migrations.AlterField(
            model_name='happybirthday',
            name='notification_type',
            field=models.CharField(default=b'e', max_length=1, verbose_name='notification method', choices=[(b'e', 'Email'), (b's', 'SMS')]),
        ),
        migrations.AlterField(
            model_name='happybirthday',
            name='sms',
            field=models.CharField(default=b'Happy $patients-age Birthday $patients-first-name!', max_length=160, null=True, verbose_name='text', blank=True),
        ),
    ]

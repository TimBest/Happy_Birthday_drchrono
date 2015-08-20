# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0003_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='cell_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='home_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='job_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='office_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='suffix',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='website',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

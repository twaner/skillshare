# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signup',
            options={'verbose_name': 'Signup', 'verbose_name_plural': 'Signups'},
        ),
        migrations.AddField(
            model_name='signup',
            name='for_you',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]

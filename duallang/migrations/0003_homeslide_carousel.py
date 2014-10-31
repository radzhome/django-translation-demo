# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duallang', '0002_homecarousel_homeslide'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslide',
            name='carousel',
            field=models.ForeignKey(default=None, to='duallang.HomeCarousel'),
            preserve_default=False,
        ),
    ]

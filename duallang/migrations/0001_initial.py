# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Name of the FAQ Topic', unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('text', models.TextField(help_text='This is a help text', verbose_name='text field test')),
            ],
            options={
                'verbose_name': 'faq topic',
                'verbose_name_plural': 'faq topics',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 00:35
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('wapps', '0002_identity_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identitytag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='identitytag',
            name='tag',
        ),
        migrations.AlterField(
            model_name='identitysettings',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='IdentityTag',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-23 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_projectimage_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(blank=True, max_length=255, upload_to='static/uploads/projects'),
        ),
    ]

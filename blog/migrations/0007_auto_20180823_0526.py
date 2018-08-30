# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-23 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170919_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('uncategorized', 'Uncategorized'), ('tutorials', 'Tutorials'), ('project-logs', 'Project Logs'), ('case-studies', 'Case Studies')], default='uncategorized', help_text='Tag your post for categorization.', max_length=60),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-24 10:59
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_project_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='content',
            field=tinymce.models.HTMLField(blank=True, help_text='To use Prism.js for code: <pre><code class="language-css">p { color: red }</code></pre>'),
        ),
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(blank=True, help_text="Your projects featured thumbnail image (Download template here: <a href='//localhost:8000/static/downloads/projectThumbTemplate.psd' downlod='//localhost:8000/static/downloads/projectThumbTemplate.psd'>Thumbnail Template</a>)", upload_to='static/uploads/projects'),
        ),
    ]

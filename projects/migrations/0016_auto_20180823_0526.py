# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-23 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20170919_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(max_length=255, upload_to='static/uploads/projects')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='permalink',
            field=models.SlugField(blank=True, max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text='Describe your project. (255 character limit)', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(help_text='Enter the link to your project. (255 character limit)', max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='stack',
            field=models.CharField(blank=True, help_text="Describe your project's used tech stack. (255 character limit)", max_length=255),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]

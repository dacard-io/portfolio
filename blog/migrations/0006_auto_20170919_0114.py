# Generated by Django 2.0.dev20170426002136 on 2017-09-19 01:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_permalink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(blank=True, help_text='To use Prism.js for code: <pre><code class="language-css">p { color: red }</code></pre>'),
        ),
    ]

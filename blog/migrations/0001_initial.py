# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(unique_for_month='pub_date', help_text='A label for url config', max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('departments', models.ManyToManyField(to='organizer.Department', blank=True, related_name='blog_posts')),
                ('tags', models.ManyToManyField(to='organizer.Tag', blank=True, related_name='blog_posts')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
                'verbose_name': 'blog post',
                'get_latest_by': 'pub_date',
            },
        ),
    ]

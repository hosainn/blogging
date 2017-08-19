# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=31)),
                ('slug', models.SlugField(help_text='a label for url config', unique=True, max_length=31)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': ['founded_date'],
            },
        ),
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('link', models.URLField(max_length=255)),
                ('department', models.ForeignKey(to='organizer.Department')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'news article',
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(unique=True, max_length=31)),
                ('slug', models.SlugField(help_text='A label for url config', unique=True, max_length=31)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='department',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='newslink',
            unique_together=set([('slug', 'department')]),
        ),
    ]

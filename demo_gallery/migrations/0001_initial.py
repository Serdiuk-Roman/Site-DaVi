# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.CharField(max_length=250)),
                ('item', models.ForeignKey(to='demo_gallery.Item')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]

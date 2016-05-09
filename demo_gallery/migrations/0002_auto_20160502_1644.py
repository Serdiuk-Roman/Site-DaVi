# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={},
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=250, verbose_name='Опись'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Картина'),
        ),
    ]

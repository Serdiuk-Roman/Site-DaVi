# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo_gallery', '0004_auto_20160502_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={},
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='caption',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]

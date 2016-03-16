# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0016_auto_20151114_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='mainContent',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='showtable',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

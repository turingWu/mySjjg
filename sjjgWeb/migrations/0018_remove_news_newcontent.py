# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0017_auto_20151114_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='newContent',
        ),
    ]

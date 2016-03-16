# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0038_auto_20160115_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadhomework',
            name='warningMess',
        ),
    ]

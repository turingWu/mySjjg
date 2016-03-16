# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0004_auto_20151114_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nav',
            name='number',
            field=models.SmallIntegerField(editable=False, auto_created=True),
        ),
    ]

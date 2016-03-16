# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0009_auto_20151114_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomment',
            name='toComment',
            field=models.ForeignKey(default=1, to='sjjgWeb.comment'),
        ),
    ]

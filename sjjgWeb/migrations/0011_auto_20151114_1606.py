# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0010_recomment_tocomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomment',
            name='toComment',
            field=models.ForeignKey(to='sjjgWeb.comment'),
        ),
    ]

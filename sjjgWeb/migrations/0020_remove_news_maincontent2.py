# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0019_news_maincontent2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='mainContent2',
        ),
    ]

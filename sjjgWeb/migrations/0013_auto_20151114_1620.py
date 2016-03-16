# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0012_news_titleimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='titleImage',
            field=models.ImageField(upload_to=b'', verbose_name=b'\xe4\xb8\xbb\xe8\xa6\x81\xe5\xb1\x95\xe7\xa4\xba\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]

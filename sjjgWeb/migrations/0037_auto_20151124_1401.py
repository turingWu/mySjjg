# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0036_auto_20151124_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecontent',
            name='files',
            field=models.FileField(null=True, upload_to=b'file', blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0021_cnav_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnav',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xe9\xa1\xb5\xe9\x9d\xa2\xe6\x98\xbe\xe7\xa4\xba\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9'),
        ),
    ]

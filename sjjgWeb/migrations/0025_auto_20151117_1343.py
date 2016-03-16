# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sjjgWeb', '0024_auto_20151116_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseMain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe6\xa0\x87\xe9\xa2\x98')),
                ('is_publish', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\xbb\xe9\xa1\xb5\xe6\x98\xbe\xe7\xa4\xba')),
                ('image', models.ImageField(upload_to=b'upload/news', null=True, verbose_name=b'\xe4\xb8\xbb\xe9\xa1\xb5\xe6\x98\xbe\xe7\xa4\xba\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u5185\u5bb9\u53d1\u5e03',
                'verbose_name_plural': '\u5185\u5bb9\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='CoursePublish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nav', models.CharField(unique=True, max_length=2, choices=[('51', '\u8bfe\u7a0b\u516c\u544a'), ('61', '\u6559\u7814\u6210\u679c')])),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u5185\u5bb9\u53d1\u5e03',
                'verbose_name_plural': '\u8bfe\u7a0b\u5185\u5bb9\u53d1\u5e03',
            },
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fileName', models.CharField(max_length=10, verbose_name=b'\xe6\x96\x87\xe4\xbb\xb6\xe4\xbb\x8b\xe7\xbb\x8d')),
                ('files', models.FileField(upload_to=b'upload/file')),
            ],
            options={
                'verbose_name': '\u6587\u4ef6\u4e0a\u4f20',
                'verbose_name_plural': '\u6587\u4ef6\u4e0a\u4f20',
            },
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nav', models.CharField(unique=True, max_length=2, choices=[('11', '\u8bfe\u7a0b\u4ecb\u7ecd'), ('12', '\u8bfe\u7a0b\u5927\u7eb2'), ('21', '\u56e2\u961f\u8d1f\u8d23\u4eba'), ('22', '\u6559\u5b66\u56e2\u961f')])),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe6\x98\xbe\xe7\xa4\xba\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'verbose_name': '\u4ecb\u7ecd\u4fe1\u606f\u7ba1\u7406',
                'verbose_name_plural': '\u4ecb\u7ecd\u4fe1\u606f\u7ba1\u7406',
            },
        ),
        migrations.CreateModel(
            name='PublishContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe6\x96\x87\xe6\x9c\xac\xe7\xbc\x96\xe8\xbe\x91')),
            ],
            options={
                'verbose_name': '\u663e\u793a\u7684\u5185\u5bb9',
                'verbose_name_plural': '\u663e\u793a\u7684\u5185\u5bb9',
            },
        ),
        migrations.CreateModel(
            name='PublishFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nav', models.CharField(unique=True, max_length=2, choices=[('31', '\u6559\u5b66\u5f55\u50cf'), ('32', '\u6388\u8bfe\u6559\u6848')])),
            ],
            options={
                'verbose_name': '\u5f55\u50cf\u548c\u6559\u6848\u4e0a\u4f20',
                'verbose_name_plural': '\u5f55\u50cf\u548c\u6559\u6848\u4e0a\u4f20',
            },
        ),
        migrations.CreateModel(
            name='PublishInformation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nav', models.CharField(unique=True, max_length=2, choices=[('13', '\u8bfe\u7a0b\u5b9e\u9a8c'), ('33', '\u8bfe\u5916\u4f5c\u4e1a'), ('41', '\u6848\u4f8b\u5e93'), ('42', '\u4e13\u9898\u8bb2\u5ea7'), ('43', '\u8d44\u6e90\u6559\u6750'), ('52', '\u8bfe\u5916\u6d3b\u52a8'), ('62', '\u6559\u7814\u6559\u6539')])),
            ],
            options={
                'verbose_name': '\u66f4\u591a\u5185\u5bb9\u53d1\u5e03',
                'verbose_name_plural': '\u66f4\u591a\u5185\u5bb9\u53d1\u5e03',
            },
        ),
        migrations.AddField(
            model_name='publishcontent',
            name='father',
            field=models.ForeignKey(to='sjjgWeb.PublishInformation'),
        ),
        migrations.AddField(
            model_name='filecontent',
            name='father',
            field=models.ForeignKey(to='sjjgWeb.PublishFile'),
        ),
        migrations.AddField(
            model_name='coursemain',
            name='father',
            field=models.ForeignKey(to='sjjgWeb.CoursePublish'),
        ),
    ]

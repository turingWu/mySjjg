# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('sex', models.BooleanField(default=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('picture', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Answer_question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe5\x8f\xb7')),
                ('question', models.CharField(max_length=150, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98')),
                ('correct', models.CharField(max_length=500, null=True, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bool_question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe5\x8f\xb7')),
                ('question', models.CharField(max_length=150, verbose_name=b'\xe9\x97\xae\xe9\xa2\x98')),
                ('correct', models.BooleanField(default=True, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88')),
            ],
        ),
        migrations.CreateModel(
            name='Choice_question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField(verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae\xe5\x8f\xb7')),
                ('question', models.CharField(max_length=200, verbose_name=b'\xe9\xa2\x98\xe7\x9b\xae')),
                ('choice_A', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9A', blank=True)),
                ('choice_B', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9B', blank=True)),
                ('choice_C', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9C', blank=True)),
                ('choice_D', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9D', blank=True)),
                ('choice_E', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9E', blank=True)),
                ('choice_F', models.CharField(max_length=100, null=True, verbose_name=b'\xe9\x80\x89\xe9\xa1\xb9F', blank=True)),
                ('correct', models.CharField(max_length=2, verbose_name=b'\xe7\xad\x94\xe6\xa1\x88', choices=[(b'A', b'A'), (b'B', b'B'), (b'C', b'C'), (b'D', b'D'), (b'E', b'E'), (b'F', b'F')])),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=500, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe5\x86\x85\xe5\xae\xb9')),
                ('commentTo', models.ManyToManyField(to='sjjgWeb.comment')),
            ],
        ),
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseName', models.CharField(max_length=10)),
                ('courseIntro', models.TextField(max_length=2000)),
                ('teachProgramming', models.FileField(upload_to=b'./upload/MyCourse')),
                ('experimentPro', models.FileField(upload_to=b'./upload/MyCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('father', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NewImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(null=True, upload_to=b'./upload/new/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('newSummary', models.CharField(max_length=200)),
                ('newContent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.SmallIntegerField(verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x88\x90\xe7\xbb\xa9')),
                ('addTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe6\x8f\x90\xe4\xba\xa4\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
        migrations.CreateModel(
            name='ShowTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98\xe6\xa6\x82\xe8\xa6\x81')),
                ('image', models.ImageField(upload_to=b'./upload/ShowTable')),
            ],
        ),
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('testsName', models.CharField(max_length=10)),
                ('content', models.FileField(upload_to=b'./upload/testData')),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField(verbose_name=b'\xe8\xaf\x95\xe5\x8d\xb7\xe7\xbc\x96\xe5\x8f\xb7')),
                ('max_score', models.SmallIntegerField(default=100, verbose_name=b'\xe8\xaf\x95\xe5\x8d\xb7\xe5\x88\x86\xe6\x95\xb0')),
                ('max_time', models.SmallIntegerField(verbose_name=b'\xe8\x80\x83\xe8\xaf\x95\xe6\x97\xb6\xe9\x97\xb4')),
                ('is_open', models.BooleanField(default=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe5\xbc\x80\xe5\x8d\xb7')),
            ],
        ),
        migrations.CreateModel(
            name='uploadHomework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.FileField(upload_to=b'./upload/homework')),
                ('homeworkId', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('s_class', models.CharField(default=b'\xe6\x9c\xaa\xe5\xa1\xab\xe5\x86\x99\xe7\x8f\xad\xe7\xba\xa7', max_length=b'10', null=True, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('sjjgWeb.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='score',
            name='testId',
            field=models.ForeignKey(to='sjjgWeb.Tests'),
        ),
        migrations.AddField(
            model_name='newimage',
            name='new',
            field=models.ForeignKey(to='sjjgWeb.News'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='choice_question',
            name='test',
            field=models.ForeignKey(to='sjjgWeb.Tests'),
        ),
        migrations.AddField(
            model_name='bool_question',
            name='test',
            field=models.ForeignKey(to='sjjgWeb.Tests'),
        ),
        migrations.AddField(
            model_name='answer_question',
            name='test',
            field=models.ForeignKey(to='sjjgWeb.Tests'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='uploadhomework',
            name='student',
            field=models.ForeignKey(to='sjjgWeb.Student'),
        ),
        migrations.AddField(
            model_name='score',
            name='student',
            field=models.ForeignKey(to='sjjgWeb.Student'),
        ),
    ]

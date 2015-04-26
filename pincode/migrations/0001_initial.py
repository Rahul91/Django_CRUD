# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pincode', models.IntegerField()),
                ('office_name', models.CharField(max_length=50)),
                ('district_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
    ]

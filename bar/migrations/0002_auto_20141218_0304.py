# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def initial(apps, schema_editor):
    Bar = apps.get_model("bar", "Bar")
    Bar.objects.create(name='data-migration')


class Migration(migrations.Migration):
    dependencies = [
        ('bar', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial),
    ]

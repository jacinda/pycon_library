# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0002_auto_20150408_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanedbook',
            name='return_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

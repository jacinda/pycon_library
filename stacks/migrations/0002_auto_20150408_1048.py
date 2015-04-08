# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='maximum_fine',
            field=models.DecimalField(default=b'25.00', help_text='Maximum amount the patron will be fined for an overdue item. This is usually the replacement cost of the item.', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='borrowing_period',
            field=models.PositiveIntegerField(default=14, help_text='Number of days this item can be borrowed before being renewed.'),
        ),
        migrations.AlterField(
            model_name='book',
            name='call_number',
            field=models.CharField(help_text='Usually Dewey Decimal or Library of Congress classification.', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='daily_fine',
            field=models.DecimalField(default=b'0.25', help_text='Amount the patron will be fined per day for an overdue library book', max_digits=4, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='book',
            name='item_number',
            field=models.PositiveIntegerField(default=1, help_text='If we have multiple copies of this book, a unique identifier for the item.'),
        ),
        migrations.AlterField(
            model_name='book',
            name='max_renewal_count',
            field=models.IntegerField(default=2, help_text='Maxmimum number of times this item can be renewed.'),
        ),
    ]

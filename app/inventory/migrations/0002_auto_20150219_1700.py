# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='polinkcustomer',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='polinkcustomer',
            name='po',
        ),
        migrations.DeleteModel(
            name='POLinkCustomer',
        ),
        migrations.AddField(
            model_name='customer',
            name='is_vendor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

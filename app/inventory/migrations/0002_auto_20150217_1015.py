# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='POLinkPurchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('po_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('item', models.ForeignKey(to='inventory.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='item',
        ),
        migrations.AddField(
            model_name='polinkpurchase',
            name='purchase',
            field=models.ForeignKey(to='inventory.Purchase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='style',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerlinkpo',
            name='po',
            field=models.ForeignKey(to='inventory.POLinkPurchase'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]

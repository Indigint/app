# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CustomerLinkPO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='inventory.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('style', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('customer', models.ForeignKey(to='inventory.Customer')),
                ('items', models.ManyToManyField(to='inventory.Purchase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('business_name', models.CharField(max_length=50)),
                ('contact', models.ForeignKey(to='inventory.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='polinkpurchase',
            name='purchase',
            field=models.ForeignKey(to='inventory.Purchase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(to='inventory.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customerlinkpo',
            name='po',
            field=models.ForeignKey(to='inventory.POLinkPurchase'),
            preserve_default=True,
        ),
    ]

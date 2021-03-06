# Generated by Django 4.0.4 on 2022-04-14 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='post',
            name='d_day',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='post',
            name='detail',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='post',
            name='n',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='one_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='target_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

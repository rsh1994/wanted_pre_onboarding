# Generated by Django 4.0.4 on 2022-04-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=128, verbose_name='     ')),
                ('server_num', models.CharField(blank=True, max_length=128, null=True, verbose_name='     ')),
                ('brand', models.CharField(blank=True, max_length=64, null=True, verbose_name='  ')),
                ('model', models.CharField(blank=True, max_length=64, null=True, verbose_name='  ')),
                ('cpus', models.IntegerField(default=0, verbose_name='cpu  ')),
                ('ram', models.IntegerField(default=0, verbose_name='    ')),
                ('disk', models.IntegerField(default=0, verbose_name='    ')),
                ('product_date', models.DateTimeField(auto_now_add=True, verbose_name='    ')),
                ('status', models.CharField(choices=[('online', '  '), ('offline', '  '), ('normal', '  '), ('abnormal', '  ')], max_length=16, verbose_name='  ')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='    ')),
                ('modified_time', models.DateTimeField(auto_now_add=True, verbose_name='    ')),
            ],
            options={
                'verbose_name': '   ',
                'verbose_name_plural': '   ',
            },
        ),
    ]

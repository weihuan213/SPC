# Generated by Django 2.2 on 2020-02-04 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0003_auto_20200204_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='erfengunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fenrongunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fenxuanunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='fujiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='huachengunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='juanraounqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='zhengjiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='zhuangpeiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='zhuyeunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

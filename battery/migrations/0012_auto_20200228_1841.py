# Generated by Django 2.2 on 2020-02-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0011_auto_20200228_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erfengunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fenrongunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fenxuanunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='fujiunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='huachengunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='juanraounqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zhengjiunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zhuangpeiunqualified',
            name='created_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='zhuyeunqualified',
            name='created_time',
            field=models.DateField(),
        ),
    ]

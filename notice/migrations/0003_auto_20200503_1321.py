# Generated by Django 2.2 on 2020-05-03 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20200503_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-create_time'], 'verbose_name': '公告', 'verbose_name_plural': '公告'},
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(max_length=500, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创造时间'),
        ),
    ]
# Generated by Django 2.2 on 2020-05-03 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200503_1330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': '昵称', 'verbose_name_plural': '昵称'},
        ),
    ]

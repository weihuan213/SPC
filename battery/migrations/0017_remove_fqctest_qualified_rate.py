# Generated by Django 2.2 on 2020-05-08 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0016_auto_20200307_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fqctest',
            name='qualified_rate',
        ),
    ]

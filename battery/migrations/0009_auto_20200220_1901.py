# Generated by Django 2.2 on 2020-02-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0008_auto_20200220_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erfeng',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='qualified_rate',
            field=models.CharField(default=0, max_length=6),
        ),
    ]
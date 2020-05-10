# Generated by Django 2.2 on 2020-02-04 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Erfeng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Fenrong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Fenxuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Fuji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Huacheng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Juanrao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='UnquaifiedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unqualified_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Zhengji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
                ('unqualified_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType')),
            ],
        ),
        migrations.CreateModel(
            name='ZhuangPei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
                ('unqualified_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType')),
            ],
        ),
        migrations.CreateModel(
            name='Zhuye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producted_time', models.DateField()),
                ('producted_num', models.IntegerField()),
                ('unqualified_num', models.IntegerField()),
                ('qualified_num', models.IntegerField()),
                ('is_delete', models.BooleanField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands')),
                ('unqualified_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType')),
            ],
        ),
        migrations.RenameModel(
            old_name='FQC_exam',
            new_name='FQCTest',
        ),
        migrations.RenameModel(
            old_name='error_information',
            new_name='WorkShopError',
        ),
        migrations.DeleteModel(
            name='er_feng',
        ),
        migrations.DeleteModel(
            name='fen_rong',
        ),
        migrations.DeleteModel(
            name='fen_xuan',
        ),
        migrations.DeleteModel(
            name='fu_ji',
        ),
        migrations.DeleteModel(
            name='hua_cheng',
        ),
        migrations.DeleteModel(
            name='juan_rao',
        ),
        migrations.DeleteModel(
            name='zheng_ji',
        ),
        migrations.DeleteModel(
            name='zhu_ye',
        ),
        migrations.DeleteModel(
            name='zhuang_pei',
        ),
        migrations.AddField(
            model_name='juanrao',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
        migrations.AddField(
            model_name='huacheng',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
        migrations.AddField(
            model_name='fuji',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
        migrations.AddField(
            model_name='fenxuan',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
        migrations.AddField(
            model_name='fenrong',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
        migrations.AddField(
            model_name='erfeng',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType'),
        ),
    ]

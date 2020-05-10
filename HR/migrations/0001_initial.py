# Generated by Django 2.2 on 2020-02-25 08:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='departments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=15, verbose_name='部门')),
            ],
        ),
        migrations.CreateModel(
            name='EducationBackground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_background', models.CharField(max_length=10, verbose_name='学历')),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=4, verbose_name='性别')),
            ],
        ),
        migrations.CreateModel(
            name='p_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('job_detail', models.CharField(default=0, max_length=30, verbose_name='职位')),
                ('home_position', models.CharField(max_length=10, verbose_name='籍贯')),
                ('work_place', models.CharField(blank=True, max_length=20, verbose_name='办公地点')),
                ('id_number', models.CharField(max_length=20, verbose_name='身份证号')),
                ('school', models.CharField(default='未知', max_length=20, verbose_name='毕业学校')),
                ('phone_number', models.CharField(default=0, max_length=15, verbose_name='电话号码')),
                ('address', models.TextField(max_length=50, verbose_name='住址')),
                ('contends', ckeditor.fields.RichTextField(default=0, verbose_name='个人经历及其他信息')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='入职时间')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否离职')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HR.departments', verbose_name='部门')),
                ('education_background', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HR.EducationBackground', verbose_name='学历')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HR.Gender', verbose_name='性别')),
            ],
        ),
    ]
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
from django.db.models import DateTimeField


class Gender(models.Model):
    gender = models.CharField(max_length=4, verbose_name='性别')

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = '性别'
        verbose_name_plural = verbose_name


class departments(models.Model):
    department = models.CharField(max_length=15, verbose_name='部门')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name


class EducationBackground(models.Model):
    education_background = models.CharField(max_length=10, verbose_name='学历')

    def __str__(self):
        return self.education_background

    class Meta:
        verbose_name = '教育背景'
        verbose_name_plural = verbose_name


class p_info(models.Model):
    #  id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, verbose_name='姓名')
    department = models.ForeignKey(departments, on_delete=models.DO_NOTHING, verbose_name='部门')
    gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING, verbose_name='性别')
    job_detail = models.CharField(max_length=30, verbose_name='职位')
    home_position = models.CharField(max_length=10, verbose_name='籍贯')
    work_place = models.CharField(max_length=20, default='不固定',blank=True, verbose_name='办公地点')
    id_number = models.CharField(max_length=10, verbose_name='身份证号')
    education_background = models.ForeignKey(EducationBackground, on_delete=models.DO_NOTHING, verbose_name='学历')
    school = models.CharField(max_length=20, default='未知', verbose_name='毕业学校')
    phone_number = models.CharField(max_length=15, verbose_name='电话号码')
    phone_in_fire = models.CharField(max_length=15, default='110', verbose_name='紧急联系人电话')
    address = models.TextField(max_length=50, verbose_name='住址')
    contends = RichTextUploadingField(verbose_name='个人经历及其他信息')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='入职时间')
    last_update_time: DateTimeField = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否离职')

    # delete_time = models.DateTimeField(verbose_name='离职时间')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = '员工信息'
        verbose_name_plural = verbose_name

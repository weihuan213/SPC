from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.departments)
class departmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'department')


@admin.register(models.Gender)
class genderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')


@admin.register(models.EducationBackground)
class EducationBackgroundAdmin(admin.ModelAdmin):
    list_display = ('id', 'education_background')


@admin.register(models.p_info)
class p_infoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'department', 'job_detail', 'work_place', 'school',
                    'home_position', 'id_number', 'created_time', 'phone_number',
                    'last_update_time', 'address', 'is_delete', 'contends')
    list_editable = ['is_delete']



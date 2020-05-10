from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.WorkShopError)
class WorkShopErrorAdmin(admin.ModelAdmin):
    list_display = ('id','happened_date','error_type','is_delete')

@admin.register(models.UnquaifiedType)
class UnquaifiedTypeAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type')

@admin.register(models.Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')

@admin.register(models.Zhengji)
class ZhengjiAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.ZhengjiUnqualified)
class ZhengjiUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Fuji)
class FujiAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.FujiUnqualified)
class FujiUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Juanrao)
class JuanraoAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.JuanraoUnqualified)
class JuanraoUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.ZhuangPei)
class ZhuangPeiAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.ZhuangPeiUnqualified)
class ZhuangPeiUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Zhuye)
class ZhuyeAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.ZhuyeUnqualified)
class ZhuyeUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Huacheng)
class HuachengAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.HuachengUnqualified)
class HuachengUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Erfeng)
class ErfengAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.ErfengUnqualified)
class ErfengUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Fenrong)
class FenrongAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.FenrongUnqualified)
class FenrongUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.Fenxuan)
class FenxuanAdmin(admin.ModelAdmin):
    list_display = ('id', 'producted_time','producted_num','unqualified_num','qualified_num','is_delete')

@admin.register(models.FenxuanUnqualified)
class FenxuanUnqualifiedAdmin(admin.ModelAdmin):
    list_display = ('id','unqualified_type','unqualified_num','created_time')

@admin.register(models.FQCTest)
class FQCTestAdmin(admin.ModelAdmin):
    list_display = ('id','ex_num','qualified_num')
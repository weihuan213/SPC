from django.db import models
from django.utils import timezone

class WorkShopError(models.Model):
    product_type = models.CharField(max_length=10, verbose_name='产品型号')
    happened_date = models.DateField(verbose_name='发生时间')
    situation_description = models.TextField(max_length=100, default=0, verbose_name='状况描述')
    reason_analysis = models.TextField(max_length=100, verbose_name='原因分析')
    measure = models.TextField(max_length=100, verbose_name='解决措施')  #
    error_type = models.CharField(max_length=10, verbose_name='错误类型')
    putting_position = models.CharField(max_length=10, verbose_name='提报工段')  #
    resp_position = models.CharField(max_length=10)
    curr_situation = models.CharField(max_length=10, verbose_name='目前状况')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '车间不良信息管理'
        verbose_name_plural = verbose_name

class UnquaifiedType(models.Model):
    unqualified_type = models.CharField(max_length=20, verbose_name='不良类型')

    def __str__(self):
        return self.unqualified_type

    class Meta:
        verbose_name = '不良类型管理'
        verbose_name_plural = verbose_name

class Brands(models.Model):
    brand = models.CharField(max_length=20, verbose_name='品牌')

    def __str__(self):
        return self.brand

    class Meta:
        verbose_name = '品牌管理'
        verbose_name_plural = verbose_name

class Zhengji(models.Model):
    procedure = models.CharField(default='正极', max_length=2, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '正极合格率统计'
        verbose_name_plural = verbose_name


class ZhengjiUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '正极不良信息管理'
        verbose_name_plural = verbose_name


class Fuji(models.Model):
    procedure = models.CharField(default='负极', max_length=2, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '负极合格率统计'
        verbose_name_plural = verbose_name


class FujiUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '负极不良信息管理'
        verbose_name_plural = verbose_name


class Juanrao(models.Model):
    procedure = models.CharField(default='卷绕车间', max_length=4, verbose_name='过程管理项目')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '卷绕车间合格率统计'
        verbose_name_plural = verbose_name


class JuanraoUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '卷绕车间不良信息管理'
        verbose_name_plural = verbose_name


class ZhuangPei(models.Model):
    procedure = models.CharField(default='装配车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '装配车间合格率统计'
        verbose_name_plural = verbose_name


class ZhuangPeiUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '装配不良信息管理'
        verbose_name_plural = verbose_name


class Zhuye(models.Model):
    procedure = models.CharField(default='注液车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='结论')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否已删除')

    class Meta:
        verbose_name = '注液车间合格率统计'
        verbose_name_plural = verbose_name


class ZhuyeUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '注液车间不良信息管理'
        verbose_name_plural = verbose_name


class Huacheng(models.Model):
    procedure = models.CharField(default='化成车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '化成车间合格率统计'
        verbose_name_plural = verbose_name


class HuachengUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '化成车间不良信息管理'
        verbose_name_plural = verbose_name


class Erfeng(models.Model):
    procedure = models.CharField(default='二封车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '二封车间合格率统计'
        verbose_name_plural = verbose_name


class ErfengUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '二封车间不良信息管理'
        verbose_name_plural = verbose_name


class Fenrong(models.Model):
    procedure = models.CharField(default='分容车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '分容车间合格率统计'
        verbose_name_plural = verbose_name


class FenrongUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '分容车间不良信息管理'
        verbose_name_plural = verbose_name


class Fenxuan(models.Model):
    procedure = models.CharField(default='分选车间', max_length=4, verbose_name='工序')
    producted_time = models.DateField(verbose_name='生产时间')
    producted_num = models.IntegerField(verbose_name='生产数')
    unqualified_num = models.IntegerField(verbose_name='不良数')
    qualified_num = models.IntegerField(verbose_name='合格数')
    brand = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, verbose_name='品牌')
    conclusion = models.TextField(default='无', verbose_name='总结')
    qualified_rate = models.CharField(default='100%', max_length=6, verbose_name='合格率')
    is_delete = models.BooleanField(default=0, verbose_name='是否删除')

    class Meta:
        verbose_name = '分选车间合格率统计'
        verbose_name_plural = verbose_name


class FenxuanUnqualified(models.Model):
    created_time = models.DateField(verbose_name='产生时间')
    unqualified_type = models.ForeignKey(UnquaifiedType, on_delete=models.DO_NOTHING, verbose_name='不合格类别')
    unqualified_num = models.IntegerField(verbose_name='不合格数量')

    class Meta:
        verbose_name = '分选车间不良信息管理'
        verbose_name_plural = verbose_name


class FQCTest(models.Model):
    ex_date = models.DateField(verbose_name='测试日期')
    ex_num = models.IntegerField(verbose_name='检验批数')
    qualified_num = models.IntegerField(verbose_name='合格批数')
    return_num = models.IntegerField(verbose_name='返工数目')

    class Meta:
        verbose_name = 'FQC抽检测试'
        verbose_name_plural = verbose_name

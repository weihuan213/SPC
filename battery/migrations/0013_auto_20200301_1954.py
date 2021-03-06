# Generated by Django 2.2 on 2020-03-01 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0012_auto_20200228_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': '品牌管理', 'verbose_name_plural': '品牌管理'},
        ),
        migrations.AlterModelOptions(
            name='erfeng',
            options={'verbose_name': '二封车间合格率统计', 'verbose_name_plural': '二封车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='erfengunqualified',
            options={'verbose_name': '二封车间不良信息管理', 'verbose_name_plural': '二封车间不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='fenrong',
            options={'verbose_name': '分容车间合格率统计', 'verbose_name_plural': '分容车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='fenrongunqualified',
            options={'verbose_name': '分容车间不良信息管理', 'verbose_name_plural': '分容车间不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='fenxuan',
            options={'verbose_name': '分选车间合格率统计', 'verbose_name_plural': '分选车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='fenxuanunqualified',
            options={'verbose_name': '分选车间不良信息管理', 'verbose_name_plural': '分选车间不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='fqctest',
            options={'verbose_name': 'FQC抽检测试', 'verbose_name_plural': 'FQC抽检测试'},
        ),
        migrations.AlterModelOptions(
            name='fuji',
            options={'verbose_name': '负极合格率统计', 'verbose_name_plural': '负极合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='fujiunqualified',
            options={'verbose_name': '负极不良信息管理', 'verbose_name_plural': '负极不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='huacheng',
            options={'verbose_name': '化成车间合格率统计', 'verbose_name_plural': '化成车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='huachengunqualified',
            options={'verbose_name': '化成车间不良信息管理', 'verbose_name_plural': '化成车间不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='juanrao',
            options={'verbose_name': '卷绕车间合格率统计', 'verbose_name_plural': '卷绕车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='juanraounqualified',
            options={'verbose_name': '卷绕车间不良信息管理', 'verbose_name_plural': '卷绕车间不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='unquaifiedtype',
            options={'verbose_name': '不合格类型管理', 'verbose_name_plural': '不合格类型管理'},
        ),
        migrations.AlterModelOptions(
            name='workshoperror',
            options={'verbose_name': '不良统计管理', 'verbose_name_plural': '不良统计管理'},
        ),
        migrations.AlterModelOptions(
            name='zhengji',
            options={'verbose_name': '正极合格率统计', 'verbose_name_plural': '正极合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='zhengjiunqualified',
            options={'verbose_name': '正极不良信息管理', 'verbose_name_plural': '正极不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='zhuangpei',
            options={'verbose_name': '装配车间合格率统计', 'verbose_name_plural': '装配车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='zhuangpeiunqualified',
            options={'verbose_name': '不良信息管理', 'verbose_name_plural': '不良信息管理'},
        ),
        migrations.AlterModelOptions(
            name='zhuye',
            options={'verbose_name': '注液车间合格率统计', 'verbose_name_plural': '注液车间合格率统计'},
        ),
        migrations.AlterModelOptions(
            name='zhuyeunqualified',
            options={'verbose_name': '注液车间不良信息管理', 'verbose_name_plural': '注液车间不良信息管理'},
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand',
            field=models.CharField(max_length=20, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='procedure',
            field=models.CharField(default='二封车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='erfeng',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='erfengunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='erfengunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='erfengunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='procedure',
            field=models.CharField(default='分容车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='fenrong',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='fenrongunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='fenrongunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='fenrongunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='procedure',
            field=models.CharField(default='分选车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='fenxuan',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='fenxuanunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='fenxuanunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='fenxuanunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='ex_date',
            field=models.DateField(verbose_name='测试日期'),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='ex_num',
            field=models.IntegerField(verbose_name='检验批数'),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格批数'),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='批次通过率'),
        ),
        migrations.AlterField(
            model_name='fqctest',
            name='return_num',
            field=models.IntegerField(verbose_name='返工数目'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='procedure',
            field=models.CharField(default='负极', max_length=2, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='fuji',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='fujiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='fujiunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='fujiunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='procedure',
            field=models.CharField(default='化成车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='huacheng',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='huachengunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='huachengunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='huachengunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='procedure',
            field=models.CharField(default='卷绕车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='juanrao',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='juanraounqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='juanraounqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='juanraounqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='unquaifiedtype',
            name='unqualified_type',
            field=models.CharField(max_length=20, verbose_name='缺陷类型'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='curr_situation',
            field=models.CharField(max_length=10, verbose_name='产生情况'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='error_type',
            field=models.CharField(max_length=10, verbose_name='错误类型'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='happened_date',
            field=models.DateField(verbose_name='出现时间'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否解除'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='measure',
            field=models.TextField(max_length=100, verbose_name='测量'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='product_type',
            field=models.CharField(max_length=10, verbose_name='产品类别'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='putting_position',
            field=models.CharField(max_length=10, verbose_name='推位'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='reason_analysis',
            field=models.TextField(max_length=100, verbose_name='原因分析'),
        ),
        migrations.AlterField(
            model_name='workshoperror',
            name='situation_description',
            field=models.TextField(default=0, max_length=100, verbose_name='状况描述'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='procedure',
            field=models.CharField(default='正极', max_length=2, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='zhengji',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='zhengjiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='zhengjiunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='zhengjiunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='procedure',
            field=models.CharField(default='装配车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='zhuangpei',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='zhuangpeiunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='zhuangpeiunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='zhuangpeiunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.Brands', verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='conclusion',
            field=models.TextField(default='无', verbose_name='结论'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='is_delete',
            field=models.BooleanField(default=0, verbose_name='是否已删除'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='procedure',
            field=models.CharField(default='注液车间', max_length=4, verbose_name='过程管理项目'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='producted_num',
            field=models.IntegerField(verbose_name='生产数'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='producted_time',
            field=models.DateField(verbose_name='生产时间'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='qualified_num',
            field=models.IntegerField(verbose_name='合格数'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='qualified_rate',
            field=models.CharField(default='100%', max_length=6, verbose_name='合格率'),
        ),
        migrations.AlterField(
            model_name='zhuye',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不良数'),
        ),
        migrations.AlterField(
            model_name='zhuyeunqualified',
            name='created_time',
            field=models.DateTimeField(auto_now=True, verbose_name='产生时间'),
        ),
        migrations.AlterField(
            model_name='zhuyeunqualified',
            name='unqualified_num',
            field=models.IntegerField(verbose_name='不合格数量'),
        ),
        migrations.AlterField(
            model_name='zhuyeunqualified',
            name='unqualified_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='battery.UnquaifiedType', verbose_name='不合格类别'),
        ),
    ]

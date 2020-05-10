from django.shortcuts import render,redirect,HttpResponse
from .utils import get_picture1_data,get_picture2_data,get_submit_time
from . import models
from HR.models import p_info, departments
from django.utils import timezone
from django.contrib import messages
import json

def week_report_first(request):
    context = {}
    department_list_all = departments.objects.all()
    context['department_list_all'] = department_list_all
    if request.user.is_authenticated:
        if request.method == "POST":
            time_submit = request.POST.get('time', '')
            first_time, last_time = get_submit_time(time_submit)
            context['work_shop_errors'] = models.WorkShopError.objects.filter(happened_date__gte = first_time,happened_date__lte = last_time)
        else:
            today = timezone.now().date()
            context['work_shop_errors'] = models.WorkShopError.objects.filter(happened_date__gte=today,
                                                                              happened_date__lte=today)
        return render(request, 'battery/week_report_first.html', context)
    else:
        return render(request,'error.html',context)

def zhengji(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time','')
        first_time,last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Zhengji,first_time,last_time)

        unqs, unqualified_data_list = get_picture2_data(models.ZhengjiUnqualified,first_time,last_time)

    else:
        today = timezone.now().date()
        dates,producted_num,qualified_num,unqualified_num\
            ,qualified_nums,unqualified_nums,quals= get_picture1_data(models.Zhengji,today,today)

        unqs,unqualified_data_list = get_picture2_data(models.ZhengjiUnqualified,today,today)

    #画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    #不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['zhengjis'] = quals
    context['zj_unqs'] = unqs
    return render(request,'battery/zhengji.html', context)

def fuji(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
        , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fuji, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.FujiUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fuji, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.FujiUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['fujis'] = quals
    context['fj_unqs'] = unqs
    return render(request, 'battery/fuji.html', context)

def juanrao(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Juanrao, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.JuanraoUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Juanrao, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.JuanraoUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['juanraos'] = quals
    context['jr_unqs'] = unqs
    return render(request, 'battery/juanrao.html', context)

def zhuangpei(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.ZhuangPei, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.ZhuangPeiUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.ZhuangPei, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.ZhuangPeiUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['zhuangpeis'] = quals
    context['zp_unqs'] = unqs
    return render(request, 'battery/zhuangpei.html', context)

def zhuye(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Zhuye, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.ZhuyeUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Zhuye, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.ZhuyeUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['zhuyes'] = quals
    context['zy_unqs'] = unqs
    return render(request, 'battery/zhuye.html', context)

def huacheng(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Huacheng, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.HuachengUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Huacheng, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.HuachengUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['huachengs'] = quals
    context['hc_unqs'] = unqs
    return render(request, 'battery/huacheng.html', context)

def erfeng(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Erfeng, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.ErfengUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Erfeng, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.ErfengUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['erfengs'] = quals
    context['ef_unqs'] = unqs
    return render(request, 'battery/erfeng.html', context)

def fenrong(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fenrong, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.FenrongUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fenrong, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.FenrongUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['fenrongs'] = quals
    context['fr_unqs'] = unqs
    return render(request,'battery/fenrong.html', context)

def fenxuan(request):
    context = {}
    if request.method == "POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fenxuan, first_time, last_time)

        unqs, unqualified_data_list = get_picture2_data(models.FenxuanUnqualified, first_time, last_time)

        # 画图需将数据转化成列表的形式(合格率统计)
    else:
        today = timezone.now().date()
        dates, producted_num, qualified_num, unqualified_num \
            , qualified_nums, unqualified_nums, quals = get_picture1_data(models.Fenxuan, today, today)

        unqs, unqualified_data_list = get_picture2_data(models.FenxuanUnqualified, today, today)

    # 画图需将数据转化成列表的形式(合格率统计)
    context['producted_num'] = producted_num
    context['qualified_num'] = qualified_num
    context['unqualified_num'] = unqualified_num
    context['dates'] = dates
    # 不良统计
    context['qualified_nums'] = qualified_nums
    context['unqualified_nums'] = unqualified_nums
    context['unqualified_data_list'] = unqualified_data_list

    context['fenxuans'] = quals
    context['fx_unqs'] = unqs
    return render(request, 'battery/fenxuan.html', context)

def fqc_test(request):
    context = {}
    time_list = []
    ex_num = []
    qua_num = []
    re_num = []
    qua_rate = []
    if request.method=="POST":
        time_submit = request.POST.get('time', '')
        first_time, last_time = get_submit_time(time_submit)
        fqcs = models.FQCTest.objects.filter(ex_date__gte=first_time,ex_date__lte=last_time)
        for fqc in fqcs:
            time_list.append(str(fqc.ex_date))
            ex_num.append(fqc.ex_num)
            qua_num.append(fqc.qualified_num)
            re_num.append(fqc.return_num)
            qua_rate.append(fqc.qualified_num/fqc.ex_num*100)
    else:
        today=timezone.now().date()
        fqcs = models.FQCTest.objects.filter(ex_date=today)
        for fqc in fqcs:
            time_list.append(str(fqc.ex_date))
            ex_num.append(fqc.ex_num)
            qua_num.append(fqc.qualified_num)
            re_num.append(fqc.return_num)
            qua_rate.append(fqc.qualified_num/fqc.ex_num*100)
    context['time_list'] = time_list
    context['ex_num'] = ex_num
    context['qua_num'] = qua_num
    context['re_num'] = re_num
    context['qua_rate'] = qua_rate
    context['fqcs'] = fqcs
    return render(request,'battery/fqc_test.html',context)


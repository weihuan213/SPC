from . import models

def get_picture1_data(obj1,first_time,last_time):
    producted_num = []
    qualified_num = []
    unqualified_num = []
    dates = []
    quals = obj1.objects.filter(producted_time__gte = first_time,producted_time__lte = last_time)
    qualified_nums = 0
    unqualified_nums = 0

    #合格率统计图的数据
    for qual in quals:
        qualified_nums = qual.qualified_num + qualified_nums
        unqualified_nums = qual.unqualified_num + unqualified_nums
        producted_num.append(qual.producted_num)
        qualified_num.append(qual.qualified_num)
        unqualified_num.append(qual.unqualified_num)
        dates.append(qual.producted_time.strftime('%m%d'))
    return dates,producted_num,qualified_num,unqualified_num,qualified_nums,unqualified_nums,quals

def get_picture2_data(obj2,first_time,last_time):
    unqs = obj2.objects.filter(created_time__gte = first_time,created_time__lte = last_time)
    #不良率统计图的数据
    unqualified_data_list = []
    unqualified_data_dict = {}
    for unq in unqs:
        if str(unq.unqualified_type) in unqualified_data_dict.keys():
            j = str(unq.unqualified_type)
            unqualified_data_dict[j] = unqualified_data_dict[j]+unq.unqualified_num
        else:
            j = str(unq.unqualified_type)
            unqualified_data_dict[j] = unq.unqualified_num
    for i in unqualified_data_dict.items():
        unqualified_data_list.append(list(i))

    '''for unq in unqs:
        unqualified_data_list.append([str(unq.unqualified_type),unq.unqualified_num])'''
    return unqs,unqualified_data_list

def get_submit_time(submit_time):
    time_zone = submit_time.split(' ')
    first_time = time_zone[0]
    last_time = time_zone[2]
    return first_time,last_time
from django.shortcuts import render, get_object_or_404
from .models import p_info, departments
from django.db.models import Count
from django.core.paginator import Paginator


# Create your views here.
def people_list_common_command(request, people_all_list):
    paginator = Paginator(people_all_list, 20)  # 20个人一页
    page_num = request.GET.get('page', 1)  # 得参
    page_of_people = paginator.get_page(page_num)
    current_page_num = page_of_people.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))  # 获取页码范围

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] + 2 <= paginator.num_pages:
        page_range.append('...')  # 添加省略号

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)  # 加上首页和尾页

    #  时间统计
    person_dates = p_info.objects.dates('created_time', 'month', order='DESC')
    person_dates_dict = {}
    for person_date in person_dates:
        person_count = p_info.objects.filter(created_time__year=person_date.year,
                                             created_time__month=person_date.month).count()
        person_dates_dict[person_date] = person_count

    context = {}
    department_list_all = departments.objects.all()
    context['department_list_all'] = department_list_all
    context['people'] = page_of_people.object_list
    context['page_of_people'] = page_of_people
    context['departments'] = departments.objects.all()
    context['page_range'] = page_range
    context['person_dates'] = person_dates_dict
    return context


def people_list(request):
    context = {}

    if request.user.is_authenticated:
        people_all_list = p_info.objects.filter(is_delete=False)
        department_list_all = departments.objects.all()
        context['department_list_all'] = department_list_all
        context = people_list_common_command(request, people_all_list)
        return render(request, 'HR/people_list.html', context)
    else:
        return render(request, 'error.html', context)


def people_with_depatments_list(request, department_pk):
    context = {}
    if request.user.is_authenticated:
        department_list_all = departments.objects.all()
        context['department_list_all'] = department_list_all
        department = get_object_or_404(departments, pk=department_pk)
        people_all_list = p_info.objects.filter(department=department, is_delete=False)
        context = people_list_common_command(request, people_all_list)
        context['department'] = department
        return render(request, 'HR/people_with_departments.html', context)
    else:
        return render(request, 'error.html', context)


def people_detail(request, people_pk):
    context = {}
    if request.user.is_authenticated:
        people = get_object_or_404(p_info, pk=people_pk)

        department_list_all = departments.objects.all()
        context['department_list_all'] = department_list_all
        context['previous_people'] = p_info.objects.filter(created_time__gt=people.created_time).last()
        context['next_people'] = p_info.objects.filter(created_time__lt=people.created_time).first()
        context['people'] = people

        response = render(request, 'HR/people_detail.html', context)

        return response
    else:
        return render(request, 'error.html', context)


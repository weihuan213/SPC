from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from HR.models import p_info, departments

def index(request):
    context = {}
    department_list_all = departments.objects.all()
    context['department_list_all'] = department_list_all
    return render(request,'index.html',context)



def search(request):
    search_words = request.GET.get('wd', '').strip()
    department_list_all = departments.objects.all()
    #  分词
    condition = None
    for word in search_words.split(' '):
        if condition is None:
            condition = Q(name__icontains=word)
        else:
            condition = condition | Q(name__icontains=word)

    search_blogs = []
    if condition is not None:
        # 搜索
        search_blogs = p_info.objects.filter(condition)

    # 分页
    paginator = Paginator(search_blogs, 5)  # 5
    page_num = request.GET.get('page', 1)  # 得参
    page_of_blogs = paginator.get_page(page_num)

    context = {}
    context['search_words'] = search_words
    context['page_of_people'] = page_of_blogs
    context['search_people_count'] = search_blogs.count()
    context['department_list_all'] = department_list_all
    return render(request, 'search.html', context)

def my_notifications(request):
    context = {}
    return render(request,'my_notifications.html',context)


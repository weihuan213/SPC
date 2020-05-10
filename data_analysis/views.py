from django.shortcuts import render,HttpResponse
from HR.models import p_info, departments
from spc import settings
import os
import json
import numpy as np
import pandas as pd
from django.contrib import messages
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Create your views here.

'''def data_analysis(request):
    context = {}
    file_root = request.session.get('file_root','')
    #try:
    print(file_root)
    df=get_df()
    context['flag'] = 1
    #except Exception:
        #messages.error(request,'你尚未导入数据或数据文件为空')
    return render(request, 'data_analysis/upload_data.html', context)'''

'''def upload_data(request):
    context = {}
    context['flag'] = ''
    return_to = reverse('upload_data')
    if request.method =='POST':
        filename = request.FILES.get('file','')
        if filename:
            excel_type = filename.name.split('.')[1]

            #上传文件格式限制
            if excel_type in ['xlsx','xls']:
                # 如果文件夹不存在，创建upload文件夹
                if not os.path.exists(settings.UPLOAD_ROOT):
                    os.makedirs(settings.UPLOAD_ROOT)
                try:
                    # 循环二进制写入
                    with open(settings.UPLOAD_ROOT + "/" + filename.name, 'wb') as f:
                        for i in filename.readlines():
                            f.write(i)
                    request.session['file_root'] = '../upload' + '/' + filename.name
                    messages.success(request,'数据导入成功')
                except Exception:
                    messages.error(request,'数据读入失败')
            else:
                messages.error(request,'文件类型错误')

        else:
            messages.error(request,'上传文件不能为空')

    return render(request,'data_analysis/upload_data.html',context)'''
#调查的各乡镇人员数量
def get_address_data(df):
    place = ['临江','竹溪','镇安','赵家','郭家','铁桥','渠口','天和','九龙山','县城内','敦好','温泉','正坝','和谦','白泉','满月','大进'
        ,'长沙','南门','义和','中和','三汇口','高桥']
    num = []
    list_df = list(df['居住的乡镇'])
    for i in range(len(place)):
        if list_df.count(i+1):
            num.append(list_df.count(i+1))
        else:
            num.append(0)
    return place,num

#教育经历统计
def get_edu_data(df):
    edu = ['小学','初中','高中','大专','本科及其以上']
    edu_data = []
    list_df = list(df['教育经历'])
    for i in range(len(edu)):
        edu_data.append({'value':list_df.count(i+1),'name':edu[i]})
    edu_data=json.dumps(edu_data,ensure_ascii=False)
    return edu_data

#统计各个乡镇在外务工情况
def get_work_info_data(df):
    place = ['临江', '竹溪', '镇安', '赵家', '郭家', '铁桥', '渠口', '天和', '九龙山', '县城内', '敦好', '温泉', '正坝', '和谦', '白泉', '满月', '大进'
        , '长沙', '南门', '义和', '中和', '三汇口', '高桥']
    in_list = []
    out_list = []
    for i in range(len(place)):
        alist = []
        blist = []
        for index, row in df.iterrows():
            if row['居住的乡镇']==i+1 and row['工作地点']==1:
                blist.append(index)
            elif row['居住的乡镇']==i+1 and row['工作地点']==2:
                alist.append(index)
        in_list.append(len(alist))
        out_list.append(len(blist))
    return in_list,out_list

#统计回家次数与务工地点的关系
def get_go_home_num(df):
    home_num_range = ['0~3','3~6','>6']
    home_0_3=[]
    home_3_6=[]
    home_over_6=[]
    for i in range(len(home_num_range)):
        alist = []
        blist = []
        for index, row in df.iterrows():
            if row['每年回家次数']==i+1 and row['工作地点']==1:
                blist.append(index)
            elif row['每年回家次数']==i+1 and row['工作地点']==2:
                alist.append(index)
        if i==0:
            home_0_3.append(['本地务工',home_num_range[i],len(alist)])
            home_0_3.append(['在外务工',home_num_range[i],len(blist)])
        elif i==1:
            home_3_6.append(['本地务工', home_num_range[i], len(alist)])
            home_3_6.append(['在外务工', home_num_range[i], len(blist)])
        elif i==2:
            home_over_6.append(['本地务工', home_num_range[i], len(alist)])
            home_over_6.append(['在外务工', home_num_range[i], len(blist)])
    a=json.dumps(home_0_3,ensure_ascii=False)
    b=json.dumps(home_3_6,ensure_ascii=False)
    c=json.dumps(home_over_6,ensure_ascii=False)
    return a,b,c

#统计性别与务工地点的关系
def get_gender_info(df):
    gender=['男','女']
    man=[]
    woman = []
    for i in range(len(gender)):
        alist = []
        blist = []
        for index, row in df.iterrows():
            if row['性别'] == i + 1 and row['工作地点'] == 1:
                blist.append(index)
            elif row['性别'] == i + 1 and row['工作地点'] == 2:
                alist.append(index)
        if i==0:
            man.append(len(alist))
            man.append(len(blist))
        elif i==1:
            woman.append(len(alist))
            woman.append(len(blist))
    return man,woman
#统计受教育程度与工作地点的关系
def edu_work(df):
    in_edu=[]
    out_edu=[]
    edu=['小学','初中','高中','大专','本科及其以上']
    for i in range(len(edu)):
        alist=[]
        blist=[]
        for index, row in df.iterrows():
            if row['教育经历'] == i+1 and row['工作地点'] == 2:
                alist.append(index)
            elif row['教育经历'] == i+1 and row['工作地点'] == 1:
                blist.append(index)
        in_edu.append({'value':len(alist),'name':edu[i]})
        out_edu.append({'value':len(blist),'name':edu[i]})
    in_edu=json.dumps(in_edu,ensure_ascii=False)
    out_edu=json.dumps(out_edu,ensure_ascii=False)
    return in_edu,out_edu

def mathine_learning(df):
    df = df.iloc[:,5:]
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.33, random_state=123)
    #使用决策树，SVC,逻辑回归,随机森林
    clf1 = DecisionTreeClassifier()
    clf1.fit(train_x, train_y)
    clf2 = SVC(probability=True, kernel='linear', cache_size=7000, max_iter=10000)
    clf2.fit(train_x, train_y)
    clf3 = LogisticRegression()
    clf3.fit(train_x, train_y)
    clf4 = RandomForestClassifier()
    clf4.fit(train_x,train_y)
    clfs=[clf1, clf2, clf3, clf4]
    accuracy_scores=[]
    for clf in clfs:
        predicted=clf.predict(test_x)
        accuracy_scores.append(accuracy_score(test_y, predicted))
    #获取重要特征值
    importance = np.round(clf4.feature_importances_,3)#保留三位有效数字
    names = train_x.columns
    importances=list(importance[importance.argsort()[::-1]])
    names = list(names[importance.argsort()[::-1]])
    decisiontree=accuracy_scores[0]
    svm=accuracy_scores[1]
    logisticregression=accuracy_scores[2]
    randomforest=accuracy_scores[3]
    return decisiontree,svm,logisticregression,randomforest,importances,names

def data_analysis(request):
    context = {}
    context['flag'] = 0
    department_list_all = departments.objects.all()
    context['department_list_all'] = department_list_all
    if request.method=='POST':
        try:
            df = pd.read_excel(request.FILES.get('excel_data'),index_col=0,header=0)
            context['flag'] = 1
            #各乡镇统计人员数量
            context['places'],context['num_of_people'] = get_address_data(df)
            #被统计人员的教育经历
            context['edu_data']=get_edu_data(df)
            #给乡镇务工人员本地、外地务工统计
            context['in_data'],context['out_data']=get_work_info_data(df)
            #统计每年回家次数与务工地点的关系
            context['home_0_3'],context['home_3_6'],context['home_over_6']=get_go_home_num(df)
            #性别与务工地点的关系
            context['man'],context['woman'] = get_gender_info(df)
            # 统计受教育程度与工作地点的关系
            context['in_edu'],context['out_edu'] = edu_work(df)
            #机器学习
            context['decisiontree'],context['svm'],context['logisticregression'],context['randomforest'],\
            context['importances'],context['names']=mathine_learning(df)
        except Exception:
            messages.error(request,'出错啦')
    return render(request,'data_analysis/upload_data.html',context)






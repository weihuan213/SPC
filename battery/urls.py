from django.urls import path
from . import views

urlpatterns = [
    path('week_report_first/',views.week_report_first,name = 'week_report_first'),
    path('week_report/zhengji/',views.zhengji,name = 'zhengji'),
    path('week_report/fuji/',views.fuji,name = 'fuji'),
    path('week_report/juanrao/',views.juanrao,name = 'juanrao'),
    path('week_report/zhuangpei/',views.zhuangpei,name = 'zhuangpei'),
    path('week_report/zhuye/',views.zhuye,name = 'zhuye'),
    path('week_report/huacheng/',views.huacheng,name = 'huacheng'),
    path('week_report/erfeng/',views.erfeng,name = 'erfeng'),
    path('week_report/fenrong/',views.fenrong,name = 'fenrong'),
    path('week_report/fenxuan/',views.fenxuan,name = 'fenxuan'),
    path('week_report/fqc_test/',views.fqc_test,name='fqc_test'),
]
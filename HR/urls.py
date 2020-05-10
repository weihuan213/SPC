from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_list, name='people_list'),
    path('department/<int:department_pk>', views.people_with_depatments_list, name='people_with_depatments_list'),
    path('<int:people_pk>', views.people_detail, name='people_detail')
]

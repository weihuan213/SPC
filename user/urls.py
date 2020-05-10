from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('user_info/', views.user_info, name='user_info'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
    path('bind_eamil/', views.bind_email, name='bind_email'),
    path('send_verification_code/',views.send_verification_code, name='send_verification_code'),
    path('change_password/',views.change_password, name='change_password'),
    path('forget_password/',views.forget_password, name='forget_password'),
]

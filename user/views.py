from django.shortcuts import render, redirect
from django.http import JsonResponse
import string
import random
import time
from django.contrib import auth
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .form import LoginForm, RegForm,ChangeNicknameForm,BindEmailForm,ChangePasswordForm,ForgetaPasswordForm
from .models import Profile


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            request.session['is_login'] = True
            return redirect(reverse('index'))

    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from',reverse('index')))

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST,request=request)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            user.save()
            #清除session
            del request.session['register_code']
            # 用户登录
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(reverse('index'))

    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)

def user_info(request):
    context = {}
    return render(request,"user/user_info.html",context)

def change_nickname(request):
    context={}
    redirect_to = request.GET.get('from',reverse('index'))
    if request.method=="POST":
        form = ChangeNicknameForm(request.POST,user=request.user)
        if form.is_valid():
            nickname_new = form.cleaned_data['nickname_new']
            profile,created = Profile.objects.get_or_create(user = request.user)
            profile.nickname = nickname_new
            profile.save()
            return redirect(redirect_to)
    else:
        form = ChangeNicknameForm()
    context['form'] = form
    context['page_title'] = '修改昵称'
    context['form_title'] = '修改昵称'
    context['submit_title'] = '修改'
    context['return_back_url'] = redirect_to
    return render(request,'form.html',context)

def bind_email(request):
    context={}
    redirect_to = request.GET.get('from',reverse('index'))
    if request.method=="POST":
        form = BindEmailForm(request.POST,request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            request.user.email = email
            request.user.save()
            # 清除session
            del request.session['bind_email_code']
            return redirect(redirect_to)
    else:
        form = BindEmailForm()
    context['form'] = form
    context['page_title'] = '绑定邮箱'
    context['form_title'] = '绑定邮箱'
    context['submit_title'] = '绑定'
    context['return_back_url'] = redirect_to
    return render(request,'user/bind_email.html',context)

def send_verification_code(request):
    email = request.GET.get('email','')
    send_for = request.GET.get('send_for','')
    data = {}
    if email != '':
        #生成验证码
        code = ''.join(random.sample(string.ascii_letters + string.digits,4))
        now = int(time.time())
        send_code_time = request.session.get('send_code_time',0)
        if now-send_code_time<30:
            data['status'] = 'ERROR'
        else:
            request.session['send_code_time'] = now
            request.session[send_for] = code
            #发送邮件验证码
            send_mail(
                '绑定邮箱',
                '验证码: %s'% code,
                '1831539195@qq.com',
                [email],
                fail_silently=False,
            )
            data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

def change_password(request):
    context = {}
    redirect_to = reverse('index')
    if request.method == "POST":
        form = ChangePasswordForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            auth.logout(request)
            return redirect(redirect_to)
    else:
        form = ChangePasswordForm()
    context['form'] = form
    context['page_title'] = '修改密码'
    context['form_title'] = '修改密码'
    context['submit_title'] = '修改'
    context['return_back_url'] = redirect_to
    return render(request, 'form.html', context)

def forget_password(request):
    context = {}
    redirect_to = reverse('login')
    if request.method == "POST":
        form = ForgetaPasswordForm(request.POST, request=request)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password']
            user = User.objects.get(email = email)
            user.set_password(new_password)
            user.save()
            # 清除session
            del request.session['forget_password_code']
            return redirect(redirect_to)
    else:
        form = ForgetaPasswordForm()
    context['form'] = form
    context['page_title'] = '重置密码'
    context['form_title'] = '重置密码'
    context['submit_title'] = '重置'
    context['return_back_url'] = redirect_to
    return render(request, 'user/forget_password.html', context)

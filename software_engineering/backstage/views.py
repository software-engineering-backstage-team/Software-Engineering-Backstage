from django.shortcuts import render, redirect
from . import models
from . import forms


# Create your views here.

def Welcome(request):
    return render(request, 'Welcome.html')


def Login(request):
    if request.session.get('is_login', None):
        return redirect('homepage')

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！(验证码)"

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = models.User.objects.filter(codename=username)
            if user:
                user = user.first()
                if user.password == password:
                    request.session['user_is_login'] = True
                    request.session['user_codename'] = user.codename
                    request.session['user_nickname'] = user.nickname
                    request.session['user_department'] = user.department_id
                    request.session['user_grant'] = user.grant
                    message = "你好，欢迎回来！"
                    print(132)
                    return redirect('backstage:Homepage')
                    # return render(request, 'Homepage.html', locals())
                else:
                    message = "密码不正确！"
            else:
                message = "用户不存在!"
                return render(request, 'Welcome.html', locals())
        return render(request, 'Login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'Login.html', locals())


def Log_out(request):
    return


def Register(request):
    return


def Homepage(request):
    if not request.session.get('user_is_login', None):
        return redirect('backstage:Login')

    if request.method == "GET":
        # announcement = models.Announcement.objects.filter(visible=True)
        return render(request, 'Homepage.html', locals())


def Send_Emails(request):
    return

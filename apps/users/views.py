# coding:utf-8
from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# reverse('register') ---> register.html
from django.db.models import Q
# Q的作用是取并集
from django.contrib.auth.hashers import make_password


from .models import User
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ResetPwdForm
from utils.common import auto_send_email, random_str_generater
from global_site.models import EmailVerifyRecord

# Create your views here.


class CustomBackend(ModelBackend):
    '''
        重写认证，使得username和email可以同时使用
    '''
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            # user = User.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
            # 大小写敏感 
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class RegisterView(View):
    def get(self, request):
        # http请求中的get方法的响应逻辑，一般就是浏览器访问网页地址。

        return render(request, 'register.html', {})

    def post(self, request):
        # http请求中的post方法的响应逻辑，一般就是表单post过来。

        register_form = RegisterForm(request.POST)
        # django 表单验证

        if register_form.is_valid():
            new_user_email = request.POST.get('email', '')
            if User.objects.get(email=new_user_email):
                return render(request, 'register.html',{
                    "msg": u"您填写的邮箱已经被注册"
                    })
            new_user = User()
            new_user.email = request.POST.get('email', '')
            new_user.username = random_str_generater(prefix="User_")
            new_password = request.POST.get('password', '')
            new_user.password = make_password(new_password)
            new_user.is_active = False
            # 新用户保存
            new_user.save()

            # 发送激活邮件
            auto_send_email(new_user.email, send_type=1)

            return HttpResponse(u'您的激活邮件已经发出，请去邮箱查收！')

        else:
            return render(request, 'register.html', {
                "register_form": register_form,
                # 表单信息回填

                "register_form_errors": sorted(register_form.errors.items())
                # 表单错误信息显示, sorted()用途是将错误的顺序改正过来，即先username errors，后password errors
                })


class ActiveUserView(View):
    def get(self, request, active_code):
        try:
            active_email_record = EmailVerifyRecord.objects.get(code=active_code)
            active_user = User.objects.get(email=active_email_record.email)
            active_user.is_active = True
            active_user.save()
            return HttpResponse(u"恭喜您！您的账户成功激活！")

        except Exception as e:
            return HttpResponse(u"验证失败")


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})
        pass

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # form 验证成功
            auth_username = request.POST['username']
            auth_password = request.POST['password']
            user = authenticate(username=auth_username, password=auth_password)
            # 验证user是否存在，如果不存在就是None,如果存在就返回username

            if user is not None:
                # 登录成功
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {"msg": u"用户未激活", })
            return render(request, 'login.html', {"msg": u"用户好像不存在", })

        else:
            # form 验证失败
            return render(request, 'login.html', {"msg": u"用户名或者密码错误", })


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

    def post(self, request):
        pass


class ForgetPwdView(View):
    def get(self, request):
        return render(request, 'forgetpwd.html', {})

    def post(self, request):
        forget_form = ForgetPwdForm(request.POST)
        if forget_form.is_valid:
            email = request.POST.get('email', "")
            if User.objects.filter(email=email):
                auto_send_email(email, send_type=2)
                return HttpResponse(u'邮件发送成功！请您检查您的邮箱！')

            else:
                return render(request, 'forgetpwd.html', {"msg": u'对不起，没有这个邮箱'})
        else:
            return render(request, 'forgetpwd.html', {"forget_form": forget_form})


class ResetPwdView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {"email": email})
        else:
            return HttpResponse(u"对不起好像没有这个邮箱")


class ModifyPwdView(View):
    def post(self, request):
        reset_form = ResetPwdForm(request.POST)
        email = request.POST.get('email', "")
        if reset_form.is_valid():
            password1 = request.POST.get('password1', "")
            password2 = request.POST.get('password2', "")
            
            if password1 == password2:
                if User.objects.filter(email=email):
                    reset_user = User.objects.get(email=email)
                    reset_user.password = make_password(password1)
                    reset_user.save()
                    return render(request, 'password_reset.html', {"msg": u'密码修改成功！', "email": email})
                else:
                    return render(request, 'password_reset.html', {"msg": u'用户不存在', "email": email})
            else:
                    return render(request, 'password_reset.html', {"msg": u'两个密码不一致', "email": email})
        else:
            return render(request, 'password_reset.html', {"reset_form_errors": sorted(reset_form.errors.items()),
                                                           "email": email})


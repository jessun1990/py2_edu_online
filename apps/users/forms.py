# coding: utf-8
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)


class RegisterForm(forms.Form):
    password = forms.CharField(required=True,
                               min_length=6,
                               max_length=20,
                               error_messages={
                                    'required': u'密码必须填写！',
                                    'min_length': u'密码至少要六位数！'
                               }
                               )
        
    email = forms.EmailField(required=True,
                             error_messages={
                                'required': u'邮箱必须填写！',
                                'invalid': u'请填写合法的邮箱地址！'
                                            }
                             )


class ForgetPwdForm(forms.Form):
    email = forms.CharField(required=True,
                            error_messages={
                                'required': u'邮箱地址必须填写',
                                'invalid': u'请填写合法的邮箱地址！'
                            }
                            )


class ResetPwdForm(forms.Form):
    email = forms.CharField(required=True,
                            error_messages={
                            'required': u'邮箱地址必须填写',
                            'invalid': u'请填写合法的邮箱地址！'
                                           }
                           )

    password1 = forms.CharField(required=True,
                            error_messages={
                            'required': u'密码必须填写'
                                           }
                               )

    password2 = forms.CharField(required=True,
                            error_messages={
                                'required': u'密码必须填写'
                           }
                           )

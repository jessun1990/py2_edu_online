# coding: utf-8
import re

from django import forms

from .models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['user', 'mobile_phone', 'course']

    def clean_mobile_phone(self):
        # 验证手机号
        mobile = self.cleaned_data['mobile_phone']
        REGEX_MOBILE = r"^(13[0-9]|14[579]|15[0-3,5-9]|17[0135678]|18[0-9])\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')

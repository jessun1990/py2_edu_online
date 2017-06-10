# coding: utf-8
from random import randint

from django.core.mail import send_mail

from py2_edu_online.settings import EMAIL_FROM
from global_site.models import EmailVerifyRecord


def random_str_generater(prefix="User", code_length=20):
    all_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    length = len(all_str) - 1
    new_username = ""
    new_username += prefix
    for i in range(code_length):
        new_username += all_str[randint(0, length)]
    return new_username


def auto_send_email(email, send_type=1):
    # send_type = 1 激活邮箱
    # send_type = 2 忘记密码
    email_record = EmailVerifyRecord()
    email_record.email = email
    email_record.code_type = send_type
    email_record.code = random_str_generater(prefix="")
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == 1:
        email_title = u"EDU_online给您发来的激活邮件"
        email_body = u"请您点击如下链接激活您的账号：http://127.0.0.1:8000/active/{0}/".format(email_record.code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    if send_type ==2:
        email_title = u"EDU_online密码重置"
        email_body = u"请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}/".format(email_record.code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

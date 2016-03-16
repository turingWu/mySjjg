#-*- coding:utf-8 -*-
from django import forms

#register Form

class RegisterForm(forms.Form):
    studentId = forms.CharField(label='学号',error_messages={"required":"学号不允许为空"},max_length=20)
    first_name = forms.CharField(max_length=20,label='名字')
    password = forms.CharField(widget=forms.PasswordInput(attrs={"required":"required",}),label='输入密码')
    surePassword = forms.CharField(widget=forms.PasswordInput(attrs={"required":"required",}),label='确认密码')
    email = forms.EmailField(max_length=20,label='邮箱')
    s_class = forms.CharField(max_length=10,label='班级')

#提交作业的form
class HomeworkForm(forms.Form):
    content = forms.FileField(label='作业上传')
    homeworkName = forms.CharField(max_length=10,label='作业题目')


class LoginForm(forms.Form):
    studentId = forms.CharField(label='学号',widget=forms.TextInput(attrs={"required":"required"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"required":"required"}),label='密码')

#test
class testForm(forms.Form):
    content = forms.Textarea()
    copy = forms.Textarea()

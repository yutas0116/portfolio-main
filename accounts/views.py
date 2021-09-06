from django.shortcuts import redirect, render
from . import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView, UserModel
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import User_Activat_Tokens
from django.contrib import messages


# 新規登録
def signup (request):
    singup_form = forms.UserForm(request.POST or None)
    if singup_form.is_valid():
        try:
            singup_form.save()
            #ここからメールの処理
            token = User_Activat_Tokens.objects.last()
            domein = request._current_scheme_host
            email =request.POST.get('email')
            subject = '仮登録完了'
            context = {'token':token,'domein':domein}
            message = render_to_string('accounts/mails/mail.txt',context,request)
            from_email = 'maburu0116@gmail.com'
            recipint_list = [email]
            send_mail(subject,message,from_email,recipint_list)
            return render(request,'accounts/provisional_registration.html')
            #　ここまで
        except ValidationError as e:
            singup_form.add_error('password',e)
    return render (request,'accounts/signup.html')


# ユーザーを有効化
def activat (request,token):
    user_activat_token = User_Activat_Tokens.objects.activat_user_by_token(token)
    return render(request,'accounts/activat.html')

#ログイン(クラスビューで簡潔に)
class UserLogin(LoginView):
    template_name = 'accounts/login.html'


#　@login_requiredはログインしないと実行できない

#　ログアウト
@login_required
def logout_User(request):
    logout(request)
    messages.success(request,'ログアウトできました')
    return redirect('board:list_thread')


# ユーザー編集
@login_required
def user_edit(request):
    user_edit_form = forms.UserEditForm(request.POST or None , instance=request.user)
    user = request.user
    if user_edit_form.is_valid():
        user_edit_form.save()
        return redirect('board:list_thread')
    return render (request,'accounts/user_edit_form.html',context={'user':user})


#　ユーザー編集(パスワード)
@login_required
def change_password(request):
    password_change_form = forms.PasswordChangeForm(request.POST or None,instance=request.user)
    user = request.user
    if password_change_form.is_valid():
        try:
             password_change_form.save()
             update_session_auth_hash(request,request.user)
        except ValidationError as e:
            password_change_form.add_error('password',e)
    return render (request,'accounts/password_change_form.html',context={'user':user,'form':password_change_form})
    
from typing_extensions import runtime
from django import forms
from .models import UserModel
from django.contrib.auth.password_validation import validate_password


#　ユーザーのフォーム
class UserForm (forms.ModelForm):
    confirm_password = forms.CharField()
    
    class Meta():
        model = UserModel
        fields = ('email','password')
#　パスワードが一致していなかった場合のエラー
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致しません')
#　ユーザーの保存
    def save(self, commit=False):
        user = super().save(commit=False)
        #バリデーション
        validate_password(self.cleaned_data['password'],user)
        #ハッシュ化
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


# ログインのフォーム
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

#　ユーザの編集のフォーム
class UserEditForm(forms.ModelForm):
    username = forms.CharField()
    email = forms.EmailField()

    class Meta():
        model = UserModel
        fields = ('username','email',)


#　ユーザのパスワード編集のフォーム
class PasswordChangeForm(forms.ModelForm):
     password = forms.CharField()
     confirm_password = forms.CharField()
    
     class Meta():
        model = UserModel
        fields = ('password',)

     def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが一致しません')

     def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'],user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user
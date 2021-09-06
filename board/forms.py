from django.db.models import fields
from django import forms
from django.db.models.fields import CharField
from django.forms.widgets import Textarea
from .models import Threads,Comments


# スレッドフォーム
class ThreadForm(forms.ModelForm):
    title = forms.CharField()

    class Meta:
        model = Threads
        fields = ('title',)


#　コメントフォーム
class CommentsForm(forms.ModelForm):
    comment = forms.CharField(label='')
    

    class Meta:
        model = Comments
        fields = ('comment',)



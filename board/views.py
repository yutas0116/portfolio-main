from django.core import paginator
from django.db import models
from .models import Threads,Comments
from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


#　スレッド投稿
def thread(request):
    thread_form = forms.ThreadForm(request.POST or None)
    if thread_form.is_valid():
        #　ここで投稿主を入れる
        thread_form.instance.user = request.user
        thread_form.save()
        return redirect ('board:list_thread')
    return render (request,'board/thread_form.html',context={'thread_form':thread_form})


# スレッドのリスト
def list_thread(request):
    threads = Threads.objects.all()
    paginator = Paginator(threads, 20)
    page_number = request.GET.get('page')
    return render (request,'board/list_thread.html',context={'page_obj':paginator.get_page(page_number),'page_number':page_number,})


#　コメント投稿
def post_comments(request,thread_id):
    comments_form = forms.CommentsForm(request.POST or None)
    thread = get_object_or_404(Threads,id=thread_id)
    comment = Comments.objects.fetch_all_comments(thread_id)
    paginator = Paginator(comment,10)
    page_number = request.GET.get('page')
    if comments_form.is_valid():
        comments_form.instance.thread = thread
        #　ユーザーがログインしていなかった時の処理
        try:
            comments_form.instance.user = request.user
        except ValueError as e:
            return render(request,'board/error.html')
        comments_form.save()
        return redirect('board:post_comments',thread_id=thread_id)
    return render(request,'board/post_comments.html',context={'thread':thread,'page_obj':paginator.get_page(page_number),'page_number':page_number})


#　スレッド検索
def search(request):
    if request.method == 'POST':
        query = request.POST.get('question')
        search_results = Threads.objects.filter(title__icontains=query).order_by('-id').all()
        return render(request,'board/search.html',context={'search_results':search_results})
    return render(request,'board/home.html')
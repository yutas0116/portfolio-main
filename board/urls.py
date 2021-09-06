from django.contrib import admin
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('thread/', views.thread,name='thread'),
    path('',views.list_thread,name='list_thread'),
    path("post_comments/<int:thread_id>",views.post_comments,name='post_comments'),
    path('home/',views.search,name='home')
]
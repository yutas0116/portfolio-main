from django.contrib import admin
from django.urls import path
from . import views
from. views import UserLogin

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('activat/<uuid:token>',views.activat,name='activat'),
    path('login/',UserLogin.as_view(),name='login'),
    path('logout/',views.logout_User,name='logout'),
    path('user_edit/',views.user_edit,name='user_edit'),
    path('change_password/',views.change_password,name='change_password')
    
]

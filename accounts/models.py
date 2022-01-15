from django import db
from django.db import models
from django.contrib.auth.models import ( AbstractBaseUser,PermissionsMixin)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime,timedelta
from django.contrib.auth.models import UserManager





#　ユーザー
class UserModel(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=40,default='名無し')
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'

# トークンの処理(マネージャー)
class User_Activat_Tokens_Manager(models.Manager):
   
    def activat_user_by_token(self,token):
        #トークンが存在するか、有効期限が切れていないか探す
        user_activat_token = self.filter(token = token,expired_at__gte = datetime.now()).first()
        #-------ここまで-------
        user = user_activat_token.user
        user.is_active = True
        user.save()
#　トークンの処理
class User_Activat_Tokens(models.Model):

    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField()
    user = models.ForeignKey('UserModel',on_delete=models.CASCADE)

    objects = User_Activat_Tokens_Manager()

    class Meta:
        db_table = 'User_Activat_Tokens'



# トークン作成
@receiver(post_save,sender=UserModel)
def pubulish_token(sender,instance,**kwargs,):
    user_activat_token = User_Activat_Tokens.objects.create(user = instance,token = str(uuid4()),expired_at = datetime.now() + timedelta(days=1))
    
    
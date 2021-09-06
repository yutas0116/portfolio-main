from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.utils import timezone



class Threads(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)   

   
    class Meta:
        db_table = 'Threads'


#　コメントのマネージャー（並べ替え）
class CommentsMnajer(models.Manager):
    def fetch_all_comments(self,thread_id):
        return self.filter(thread_id=thread_id).order_by('-id')


class  Comments(models.Model):
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    thread = models.ForeignKey('Threads',on_delete=models.CASCADE)
    create_at = models.DateTimeField(default=timezone.now)
    
    objects = CommentsMnajer()
    class Meta:
         db_table = 'Comments'

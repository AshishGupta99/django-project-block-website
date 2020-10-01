from django.db import models
from .forumuser import ForumUser
#crearte your models here
class Blocks(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  user_id = models.ForeignKey(ForumUser,on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
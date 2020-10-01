from django.db import models
from .forumuser import ForumUser
from .blocks import Blocks
# Create your models here.
class Questions (models.Model):
  question = models.TextField()
  user_id = models.ForeignKey(ForumUser,on_delete=models.CASCADE)
  block_obj = models.ForeignKey(Blocks,on_delete=models.CASCADE)
  def __str__(self):
    return self.question
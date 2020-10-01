from django.db import models
from .forumuser import ForumUser
from .blocks import Blocks
from .questions import Questions
# Create your models here.

class Answers(models.Model):
  answer = models.TextField()
  user_id = models.ForeignKey(ForumUser,on_delete=models.CASCADE)
  block_obj = models.ForeignKey(Blocks,on_delete=models.CASCADE)
  question_obj = models.ForeignKey(Questions,on_delete=models.CASCADE)
  def __str__(self):
    return self.answer
  
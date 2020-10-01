from django.db import models

# Create your models here.
class ForumUser(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  user_name = models.CharField(max_length=50)
  e_mail = models.EmailField()
  password = models.CharField(max_length=500)
  
  def __str__(self):
    return self.user_name
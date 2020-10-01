from django.contrib import admin
from .models.forumuser import ForumUser
from .models.blocks import Blocks
from .models.questions import Questions
from .models.answers import Answers
# Register your models here.
class tableForumUser(admin.ModelAdmin):
  list_display = ['id','user_name','e_mail','first_name','last_name','password']
  
class tableBlocks(admin.ModelAdmin):
  list_display = ['id','user_id','title','description']
  
class tableQuestions(admin.ModelAdmin):
  list_display = ['id','user_id','block_obj','question']

class tableAnswers(admin.ModelAdmin):
  list_display = ['id','user_id','block_obj','question_obj','answer']

admin.site.register(ForumUser,tableForumUser)
admin.site.register(Blocks,tableBlocks)
admin.site.register(Questions,tableQuestions)
admin.site.register(Answers,tableAnswers)

#urls.py of app(forumApp)

from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns = [
      path('',views.forumApp,name='forumApp'),
      path('signup',views.signup,name='signup'),
      path('login',views.login,name='login'),
      path('logout',views.logout,name='logout'),
      path('questions',views.question,name='question'),
      path('addBlock',views.addBlock,name='addBlock'),
      path('addQuestion',views.addQuestion,name='addQuestion'),
      path('answers',views.answers,name='answers'),
      path('addAns',views.addAns,name='addAns')
      #path('authentication',views.authentication,name="authentication")
  ]
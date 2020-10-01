from django.shortcuts import render,HttpResponse,redirect
from .models.forumuser import ForumUser
from django.contrib.auth.hashers import make_password,check_password
from .models.blocks import Blocks
from .models.questions import Questions
from .models.answers import Answers
# Create your views here.
def forumApp(request):
  login = False
  session = None
  allBlocks = Blocks.objects.all()
  print(allBlocks)
  try:
    session = {
      "username":request.session['usernamelgn'],
      "firstname":request.session['fname'],
      "lastname":request.session['lname'],
      "user_id":request.session['user_id'],
      "email":request.session['email'],
      "isLogin":True
    }
    
    login = True
  except:
    print('annonymous user')
    return render(request,'home/home.html',{"blocks":allBlocks})
  
  if login:
    myBlocks = Blocks.objects.filter(user_id=request.session['user_id'])
    #print(myBlocks[0],myBlocks[0].id)
    return render(request,"home/home.html",{"session":session,"blocks":allBlocks,"myBlocks":myBlocks})
  
def signup(request):
  if request.method == "POST":
    firstname = request.POST['lname']
    lastname = request.POST['fname']
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    
    allBlocks = Blocks.objects.all()
    
    signup_data = {
      "fname":firstname,
      "lname":lastname,
      "username":username,
      "email":email,
      "password1":password1,
      "password2":password2
    }
    
    error = None
    if not firstname:
      error = "first name is required"
    elif not lastname:
      error = "last name is required"
    elif not username:
      error = "username is required"
    elif not email:
      error = "email id is required"
    
    
    if not error:
      if password1 == password2:
        fetchUser = ForumUser.objects.filter(user_name=username)
        
        if fetchUser.exists():
          msg = "user name is already taken, please enter unique username"
          return render(request,'home/home.html',{"error":msg,"data":signup_data,"blocks":allBlocks})
        
        elif ForumUser.objects.filter(e_mail=email).exists():
          msg = "email is already in use , please enter unique email id"
          return render(request,'home/home.html',{"error":msg,"data":signup_data,"blocks":allBlocks})
        
        elif len(password1) < 5:
          msg = "you password is too short enter strong password"
          return render(request,'home/home.html',{"error":msg,"data":signup_data,"blocks":allBlocks})
        
        else:
          forumuser = ForumUser(first_name=firstname,last_name=lastname,user_name=username,e_mail=email,password=make_password(password1))
          forumuser.save()
          return redirect('/')
          
      else:
        return render(request,'home/home.html',{"error":"password is not matches, please again enter password","data":signup_data,"blocks":allBlocks})
   
    else:
      return render(request,'home/home.html',{"error":error,"data":signup_data,"blocks":allBlocks})
  else:  
    return redirect('/')

  
def login(request):
  if request.method == "POST":
    username = request.POST['usernamelgn']
    password = request.POST['password']
    data2 = {
      "username":username,
      "password":password
    }
    allBlocks = Blocks.objects.all()
    fetchUser = ForumUser.objects.filter(user_name=username)
    check_pass = check_password(password,fetchUser[0].password)
    if fetchUser.exists() and check_pass:
      request.session['fname'] = fetchUser[0].first_name
      request.session['lname'] = fetchUser[0].last_name
      request.session['usernamelgn'] = fetchUser[0].user_name
      request.session['user_id'] = fetchUser[0].id
      request.session['email'] = fetchUser[0].e_mail
      return redirect('/')
      
    elif fetchUser.exists() and not check_pass:
      msg = "wrong password , enter again"
      return render(request,'home/home.html',{"error":msg,"data2":data2,"blocks":allBlocks})
      
    elif check_pass and not fetchUser.exists():
      msg = "wrong username , enter again"
      return render(request,'home/home.html',{"error":msg,"data2":data2,"blocks":allBlocks})
      
    else:
      msg = "wrong password and username ,enter again"
      return render(request,'home/home.html',{"error":msg,"data2":data2,"blocks":allBlocks})
     
  else:  
    return redirect('/')
 
 
def logout(request):
  request.session.clear()
  return redirect('/')

  
def question(request):
  if request.method == "GET":
    login = False
    session = None
    allBlocks = Blocks.objects.all()
    getData = request.GET['block']
    getObj = Blocks.objects.filter(title=getData)[0]
    #print("get object is ",getObj.user_id.user_name)
    #print(allBlocks)
    allQuestions = Questions.objects.filter(block_obj=getObj)
    print("filtered object ",allQuestions)
    try:
      session = {
        "username":request.session['usernamelgn'],
        "firstname":request.session['fname'],
        "lastname":request.session['lname'],
        "user_id":request.session['user_id'],
        "email":request.session['email'],
        "isLogin":True
      }
    
      login = True
    except:
      print('annonymous user')
      return render(request,'home/questions.html',{"getObj":getObj,"allQuestions":allQuestions})
  
    if login:
      return render(request,'home/questions.html',{"session":session,"getObj":getObj,"allQuestions":allQuestions})


def addBlock(request):
  if request.method == "POST":
    fetchUser = ForumUser.objects.filter(user_name=request.session['usernamelgn'])[0]
    newBlock = Blocks(title=request.POST['title'],description=request.POST['description'],user_id=fetchUser)
    #print("user name",request.session['usernamelgn'])
    newBlock.save()
    return redirect('/')
  else:
    return redirect('/')


def addQuestion(request):
  if request.method == "POST":
    question = request.POST['question']
    block_title = request.POST['title_id']
    print("post block title",block_title)
    fetchUser = ForumUser.objects.filter(user_name=request.session['usernamelgn'])[0]
    print("session user q",fetchUser)
    fetchBlock = Blocks.objects.filter(title=block_title)[0]
    print("block qx",fetchBlock)
    print("block user ",fetchBlock.user_id)
    question_obj = Questions(question=question,user_id=fetchUser,block_obj=fetchBlock)
    question_obj.save()
    #return redirect('/question?block='+fetchBlock)
    return redirect(f"/questions?block={fetchBlock}")
    #return HttpResponse("Your question submitted")


def answers(request):
  login = False
  session = None
  if request.method == "GET":
    question = request.GET['question']
    block = request.GET['block']
    print(question,block)
    headData = {
      "block":block,
      "question":question
    }
    fetchBlock_obj = Blocks.objects.filter(title=block)[0]
    print(fetchBlock_obj)
    fetchQuestion_obj = Questions.objects.filter(question=question,block_obj=fetchBlock_obj)[0]
    print('fetch question',fetchQuestion_obj)
    allAnswers = Answers.objects.filter(block_obj=fetchBlock_obj,question_obj=fetchQuestion_obj)
    print(allAnswers)
    try:
      session = {
        "username":request.session['usernamelgn'],
        "firstname":request.session['fname'],
        "lastname":request.session['lname'],
        "user_id":request.session['user_id'],
        "email":request.session['email'],
        "isLogin":True
      }
      login = True
    
    except:
      print("anonymous user")
      return render(request,'home/answer.html',{'headData':headData,'allAnswers':allAnswers})
    
    if login:
      return render(request,'home/answer.html',{'headData':headData,'session':session,'allAnswers':allAnswers})

def addAns(request):
  if request.method == 'POST':
    answer = request.POST['answer']
    post_question = request.POST['post_question']
    post_block = request.POST['post_block']
    logined_user = request.session['usernamelgn']
    
    fetchBlock_obj = Blocks.objects.filter(title=post_block)[0]
    fetchQuestion_obj = Questions.objects.filter(question=post_question)[0]
    fetchUser_obj = ForumUser.objects.filter(user_name=logined_user)[0]
    
    
    ans_obj = Answers(answer=answer,user_id=fetchUser_obj,block_obj=fetchBlock_obj,question_obj=fetchQuestion_obj)
    ans_obj.save()
    return redirect(f"/answers?question={post_question}&block={post_block}")
  #return HttpResponse('adding postX data ')
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from Dashboard.views import updateuser
from Dashboard.views import dashboard,updateuser,contactdetails
from .forms import LoginForm,Usercreationform,RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.hashers import make_password
from Userprofiles.models import Curent_user_management
app_name = dashboard
User = get_user_model()
def mainsite(request):
    return render(request,'mainpage/index.html')

def loginuser(request):
    
    if request.user.is_authenticated:
        return redirect(dashboard)
    else:
        form = LoginForm(request.POST or None)
        msg = None
        if request.method == 'POST':
            if form.is_valid():
                    username = request.POST.get('username')
                    password = request.POST.get('password')
                    

                    user = authenticate(request,username=username,password=password)
                    print("authenticated ")
                    print(user)
                    if user is not None:
                      login(request,user)
                      print("logged in")
                      return redirect(dashboard)
                    else :
                        try :
                            usercheck = User.objects.get(username=username)
                            msg = 'Invalid password'
                        except:
                            msg = 'User account does not exsists'
                    # else:
                    #     msg = "error"
            else:
              msg = 'Error in form'

        context = {"form":form,"msg":msg}
        return render(request,'accounts/login.html',context)

# def registeruser(request):
#     msg = None
#     register = Usercreationform(request.POST)
#     if request.method == 'POST':
#         register = Usercreationform(request.POST)
#         if register.is_valid():
#             register.save()
#             username = request.POST.get('username')
#             password = request.POST.get('password1')
#             user = authenticate(request,username = username, password = password)
#             if user is not None:
#                 login(request,user)
#                 return redirect(updateuser)
#             else:
#                 msg = "User account does not exsists"
#         else:
#             msg = "Registration not successfull"
#     else:
#         msg = "request methord not valid"
#     context = {"form":register,"msg":msg}
#     return render(request,'accounts/register.html',context)
            
def registerForm(request):
    msg = None
    form =  RegisterForm(request.POST)
    current_users = Curent_user_management()
    if request.user.is_authenticated:
        return redirect(dashboard)
    else:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                raw_password= password
                email = request.POST.get('email')
                password_confirmation = request.POST.get('password_confirmation')
                if password == None or password_confirmation == None :
                    msg = "Please validate your password"
                elif password != password_confirmation:
                    msg = "passwords didn't match"
                if password_confirmation == password:
                
                        password = make_password(password)
                        user = User.objects.create(username = username,email = email,password=password)
                        print("user registration")
                        user.save()
                        print("user registered")
                        userlogin = authenticate(request,username=username,password=raw_password)
                        print("user authentication")
                        login(request,userlogin)
                        print("user login")
                        return redirect(contactdetails)
                        print("re directed succefulley")
            else:
                msg = "form is not valid"
        
        context = {"form":form,"msg":msg}
    return render(request,'accounts/register.html',context)

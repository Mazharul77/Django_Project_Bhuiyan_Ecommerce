from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def login_func(request):
    if request.method=='POST':
      name = request.POST['name']  
      password = request.POST['password']

      user = authenticate(request, username = name, password = password)

      if user is not None:
          login(request, user)
          return redirect('Emp.desig')
      else:
          messages.error(request, 'Invalid User Name or Password !!!')
          print('Invalid UserName or Password')          
    return render(request, 'authentication/login.html')


def registration_func(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=name).exists():
                messages.error(request, 'Sorry! User Name Already Exists!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Sorry! Same Email Address Already Exists!')
            else:
                user = User.objects.create_user(username=name, password=password, email=email)
                user.save()
                messages.success(request, 'Successfully, Your new account has been created !!!')
                return redirect('login')
            
        else:
            messages.error(request, 'Password And Confirm_Password are not matched !')

    return render(request, 'authentication/registration.html')

def forgot_func(request):
    return render(request, 'authentication/forgotPass.html')

def logout_func(request):
    logout(request)
    messages.success(request, 'Your Account Successfully Logged Out !')
    return redirect('login')

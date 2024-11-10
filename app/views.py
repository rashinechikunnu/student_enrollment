from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Login
# Create your views here.

def home(request):
    return render(request,'index.html')


# login 
def log_in(request):

    if request.method == "POST":
        user_name = request.POST.get('user_name')
        print(user_name)
        user_password = request.POST.get('password')
        print(user_password)
        
        user_click=authenticate(request,username=user_name,password=user_password)
        print(user_click)

        if user_click is not None:
            login(request,user_click)
        
            if user_click.is_staff:
                return redirect('admin_home')
            
            elif user_click.is_student:
                return redirect('list_studnet')
            
       
        else:
            messages.info(request,'invalid username and password')
    return render(request,'login.html')
    

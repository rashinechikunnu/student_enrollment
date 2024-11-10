from django.shortcuts import render,redirect
from .forms import studentForms,LoginForms



# student account creation
def student_account_creation(request):
    
    l_form = LoginForms()
    s_form = studentForms()

    if request.method == "POST":
        l_form = LoginForms(request.POST)
        
        s_form = studentForms(request.POST)
        
        if l_form.is_valid() and s_form.is_valid():
            a = l_form.save(commit=False)
            a.is_student = True
            a.save()
            user1= s_form.save(commit=False)
            user1.user=a
            user1.save()
        
            return redirect('list_studnet')
        
    return render(request,"student/register.html",{'l_form':l_form,'s_form':s_form})


# list
def view_data(request):
    return render(request,'student/list.html')
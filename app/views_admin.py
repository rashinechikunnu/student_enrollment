from django.shortcuts import render
from .models import student_data
def admin_home(request):
    return render(request,'admin/dash_board.html')



# view students 
def std_views(request):
    std = student_data.objects.all()
    return render(request,'admin/std_table.html',{'std':std})
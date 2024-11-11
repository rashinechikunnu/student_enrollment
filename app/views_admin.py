from django.shortcuts import render,redirect
from .models import student_data,Class_room,Subject
from .forms import class_room_Forms
def admin_home(request):
    return render(request,'admin/dash_board.html')



# view students 
def std_views(request):
    std = student_data.objects.all()
    return render(request,'admin/std_table.html',{'std':std})

# create class room
def create_class_room(request):
    if request.method == 'POST':
        cls_form = class_room_Forms(request.POST)
        if cls_form.is_valid():
            cls_form.save()
            return redirect('class_rooms')
    
    else :
        cls_form = class_room_Forms()

    return render(request,'admin/create_class_room.html',{'cls_form':cls_form})

# create class room
def class_rooms(request):
    room = Class_room.objects.all()
    return render(request,"admin/class_room.html",{"room_class":room})

# subject


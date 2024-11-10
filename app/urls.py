from django.urls import path
from . import views,views_student,views_admin

urlpatterns = [
    path('',views.home,name='home'),
    # student registration
    path('register',views_student.student_account_creation,name='register'),
    # login page
    path('login',views.log_in,name='login'),
    

    # admin page
    # home
    path('admin_home',views_admin.admin_home,name='admin_home'),
    # all studnet table
    path('std_table',views_admin.std_views,name="std_table"),


    # student page
    # view student data
    path('list_student',views_student.view_data,name='list_studnet'), 
]

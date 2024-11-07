from django.urls import path
from . import views,views_student

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views_student.student_account_creation,name='register'),
    path('login',views.log_in,name='login')
]

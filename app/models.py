from django.db import models
from django.contrib.auth.models import AbstractUser
# LOGIN

class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
   
    
# customer models

class student_data(models.Model):
    user = models.ForeignKey(Login,on_delete= models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=10)
    date_of_birth=models.CharField(max_length=10)
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    sex = models.IntegerField(choices=GENDER_CHOICES,null=True,blank=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.first_name


class Class_room(models.Model):
    name_class = models.CharField(max_length=2)  
    section = models.CharField(max_length=1)  

    def __str__(self):
        return self.name_class


class Subject(models.Model):
    name = models.CharField(max_length=100)  
    class_assigned = models.ForeignKey(Class_room, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return self.name
    

class Enrollment(models.Model):
    student = models.ForeignKey(student_data, on_delete=models.CASCADE)
    class_assigned = models.ForeignKey(Class_room, on_delete=models.CASCADE)
    subject_assigned = models.ForeignKey(Subject, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.student






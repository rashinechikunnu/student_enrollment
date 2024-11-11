from django import forms
from .models import student_data,Login,Class_room,Subject
from django.contrib.auth.forms import UserCreationForm





class LoginForms(UserCreationForm):
    username=forms.CharField()
    password1=forms.CharField(label="password", widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2=forms.CharField(label="password",widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields =('username',"password1","password2") 

class studentForms(forms.ModelForm):
    
    class Meta:
        model = student_data
        fields ="__all__"
        exclude = ("user",)


class class_room_Forms(forms.ModelForm):
    
    class Meta:
        model = Class_room
        fields ="__all__"
       

class subject_Forms(forms.ModelForm):
    
    class Meta:
        model = Subject
        fields ="__all__"
       
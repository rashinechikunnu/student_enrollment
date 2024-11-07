from django import forms
from .models import student_data,Login
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
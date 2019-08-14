from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    Password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']
class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=['mobile_number','profile_pic']
    
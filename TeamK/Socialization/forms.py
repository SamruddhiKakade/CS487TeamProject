from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'password1', 'password2']

# class ProfileForm(forms.Form): 
#     class Meta:
#         model = Profile
#         fields = ['Year','Major']


class searchUserForm(forms.Form):
    name = forms.CharField(label='', max_length=20)

class searchResultForm(forms.Form):
    name = forms.CharField(label='', max_length=20)

class chatForm(forms.Form):  
    username = forms.CharField(label='', max_length=100)
    
class messageForm(forms.Form):  
    message = forms.CharField(label='', max_length=1000)



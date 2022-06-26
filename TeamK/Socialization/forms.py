from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class informationForm(forms.Form):  
    name = forms.CharField(label='', max_length=20)
    year = forms.IntegerField(label='')
    major = forms.CharField(label='', max_length=100)

class messageForm(forms.Form): 
    message = forms.CharField(label='', max_length=1000)

class userNameForm(forms.Form): 
    userName = forms.CharField(label='', max_length=20)

class searchUserForm(forms.Form):
    name = forms.CharField(label='', max_length=20)

class searchResultForm(forms.Form):
    choice = forms.CharField(label='', max_length=20)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class InfoForm(forms.Form):
    # Username = forms.CharField(label='Username', max_length=1000)
    # Password = forms.CharField(label='Password', max_length=50)
    Name = forms.CharField(label='Name', max_length=20)
    Year = forms.IntegerField(label='Year')
    Major = forms.CharField(label='Major', max_length=100)

class ChatMessageForm(forms.Form):
    Message = forms.CharField(label='Message', max_length=1000)

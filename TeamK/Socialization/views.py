from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from models import User
from .forms import InfoForm,UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
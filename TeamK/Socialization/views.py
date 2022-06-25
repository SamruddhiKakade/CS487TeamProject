from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import User
from Socialization.forms import informationForm,UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def userAcct(request):
    return render(request, 'test.html')
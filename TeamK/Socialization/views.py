from hmac import new
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import ChatMessage,Information
from Socialization.forms import informationForm,UserRegisterForm
from django.contrib.auth.models import User



# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('information')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def userAcct(request):
    return render(request, 'test.html')

def information(request):
    if request.method == 'POST':
        temp = request.user
        form = informationForm(request.POST)
        if form.is_valid():
            newInformation = Information(
                person = temp,
                Name = form.cleaned_data['name'],
                Year = form.cleaned_data['year'],
                Major = form.cleaned_data['major'],
            )
            newInformation.save()
            info = Information.objects.filter(person = request.user)
            context = {
                'info': info
            }
            return redirect('account',context)
    else:
        form = informationForm()
    return render(request, 'information.html', {'form': form})


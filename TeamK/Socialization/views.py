from hmac import new
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import User
from Socialization.forms import informationForm,UserRegisterForm
from TeamK.Socialization.models import Information


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
        form = informationForm(request.POST)
        if form.is_valid():
            newInformation = Information(
                user = request.user,
                Name = form.cleaned_data['name'],
                Year = form.cleaned_data['year'],
                Major = form.cleaned_data['major'],
            )
            newInformation.save()
            info = Information.objects.filter(user = request.user)
            context = {
                'info': info
            }
            return redirect('account',context)
    else:
        form = informationForm()
    return render(request, 'information.html', {'form': form})


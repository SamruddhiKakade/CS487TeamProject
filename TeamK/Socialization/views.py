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
            temp = form.save()
        form1 = informationForm(request.POST)
        if form1.is_valid():
            newInformation = Information(
                person = temp,
                Name = form1.cleaned_data['name'],
                Year = form1.cleaned_data['year'],
                Major = form1.cleaned_data['major'],
            )
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    info = Information.objects.filter(person = request.user)
    context = {
        'info': info
    }
    return render(request, 'home.html',context)


from hmac import new
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import ChatMessage,Information
from Socialization.forms import informationForm,UserRegisterForm
from django.contrib.auth.models import User
from django.db.models import Q



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
            newInformation.save
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

def newMessage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":  
        newMessage = ChatMessage(                
            sender = request.user,                                                     
            receiver = '',
            body = request.POST.get('message'),                
        )     
        newMessage.save()  

def showInbox(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        messages1 = ChatMessage.objects.filter(Q(sender = request.user)) 
        messages2 = ChatMessage.objects.filter(Q(receiver = request.user)) 
        context = {    
            'recieverNames': messages1,
            'senderNames': messages2  
        }  
        return render(request, 'inbox.html', context)

def showMessages(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        user1 = ''
        messagesList = ChatMessage.objects.filter(Q(Q(receiver = request.user)&Q(sender = user1))|Q(Q(sender = request.user)&Q(reciever = user1)))
        context = {    
            'messages' : messagesList
        }  
        return render(request, 'chat.html', context)


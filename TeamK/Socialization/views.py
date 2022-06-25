from hmac import new
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import ChatMessage,Information
from Socialization.forms import informationForm,UserRegisterForm,messageForm,userNameForm
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
        form1 = informationForm()
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
        form = messageForm(request.POST)
        if form.is_valid(): 
            newMessage = ChatMessage(                
                sender = request.user,                                                     
                receiver = '',
                message = form.cleaned_data['message'],                
            )     
            newMessage.save() 
            return redirect('showMessages')
    else:
        form = messageForm()
    return render(request, 'chat.html', {'form': form})

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

def searchUser(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST": 
        form = userNameForm(request.POST)
        if form.is_valid():  
            user1 = form.cleaned_data['userName']
            user2 = User.objects.filter(username = user1)
            context = {    
            'user' : user2
        }  
        return render(request, 'page.html', context)
    else:
        form = userNameForm()
    return render(request, 'page.html', {'form': form})

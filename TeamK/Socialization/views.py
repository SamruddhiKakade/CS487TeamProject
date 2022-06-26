from hmac import new
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from Socialization.models import ChatMessage,Information
from Socialization.forms import informationForm,UserRegisterForm,messageForm,userNameForm,searchUserForm,searchResultForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
@csrf_exempt
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

@csrf_exempt
def home(request):
    info = Information.objects.filter(person = request.user)
    context = {
        'info': info
    }
    return render(request, 'home.html',context)

@csrf_exempt
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

@csrf_exempt
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

@csrf_exempt
def showMessages(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = searchResultForm(request.POST)
        user1 = form.cleaned_data['name']
        messagesList = ChatMessage.objects.filter(Q(Q(receiver = request.user)&Q(sender = user1)) | Q(Q(sender = request.user)&Q(reciever = user1)))
        context = {
            'receiver' : user1,
            'messages' : messagesList
        }  
        return render(request, 'chat.html', context)

@csrf_exempt
def openSearch(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        return render(request, 'searchQuery.html')

@csrf_exempt
def searchUser(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = searchUserForm(request.POST)
        print(form.is_valid())
        # if form.is_valid():
        #     name = form.cleaned_data['name']
        #     matches = User.objects.filter(Q(username__contains=name) | Q(Name__contains=name))
        #     context = {
        #         'Names' : list(matches.Name),
        #         'Usernames' : list(matches.username)
        #     }
        name = form.cleaned_data['name']
        matches = User.objects.filter(Q(username__contains=name))
        context = {
            'Usernames': list(matches.username)
        }
        return render(request, 'searchResult.html', context)

@csrf_exempt
def searchResults(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        form = searchUserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            context = {
                'matches' : User.objects.filter(Q(username__contains=name) | Q(Name__contains=name))}

        return render(request, 'searchResult.html', context)

@csrf_exempt
def showChats(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        context = {

        }



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


# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return render_to_response('search.html', ctx)
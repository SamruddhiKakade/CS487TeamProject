from django.shortcuts import render, redirect
from Socialization.models import Chat,Message
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, searchUserForm,chatForm,messageForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        # profile_form = ProfileForm(request.POST)
        # profile = profile_form.save(commit=False)
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            # user.profile = profile
            user.save()
            username = user.username
            messages.success(request, f'Hello {username}! Your account has been created. You are now ready to log in.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        # profile_form = ProfileForm()
    return render(
        request, 
        'register.html', 
        {
            'user_form': user_form,
            # 'profile_form': profile_form
        }
    )

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:

#         # can now set user_status attribute
#         Profile.objects.update_or_create(
#             user=instance,
#             user_status=instance.profile.user_status,
#         )


# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()

@csrf_exempt
def home(request):
    return render(request, 'home.html')

# @csrf_exempt
# def profile(request):
#     info = Information.objects.filter(person = request.user)
#     context = {
#         'info': info 
#     }
#     return render(request, 'profile.html',context)



@csrf_exempt
def openSearch(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        return render(request, 'searchQuery.html')


def search(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = searchUserForm()    
        context = {      
            'form': form    
        } 
        return render(request, 'searchQuery.html', context)
    if request.method == "POST":
        form = searchUserForm(request.POST)
        form1 = chatForm()
        if form.is_valid():
            name = form.cleaned_data['name']
        context = {
            'Usernames' : User.objects.filter(Q(username__contains=name) | Q(Name__contains=name)),
            'form':form1
        }
        return render(request, 'NewChat.html',context )

def newChat(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = chatForm()    
        context = {      
            'form': form    
        } 
        return render(request, 'NewChat.html', context)
    if request.method == "POST":
        form = chatForm(request.POST)    
        username = request.POST.get('username')    
        try:      
            receiver = User.objects.get(username = username)      
            if Chat.objects.filter(user1 = request.user, user2 = receiver).exists():
                chat = Chat.objects.filter(user1 = request.user, user2 = receiver)[0]
                chatpk = chat.pk
                return redirect('chat', pk = chatpk)
            elif Chat.objects.filter(user1 = receiver, user2 = request.user).exists():        
                chat = Chat.objects.filter(user1 = receiver, user2 = request.user)[0]
                chatpk = chat.pk
                return redirect('chat', pk = chatpk)
            else:        
                newchat = Chat(          
                    user1 = request.user,          
                    user2 = receiver        
                )        
                newchat.save()
                chatpk = newchat.pk
                return redirect('chat', pk = chatpk)    
        except:      
            return redirect('newchat')    
    
def showChats(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        chats = Chat.objects.filter(Q(user1 = request.user) | Q(user2 = request.user)) 
        context = {    
            'chats': chats  
        }  
        return render(request, 'Messages.html', context)
           
def newMessage(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        chat = Chat.objects.get(pk = pk)
        if chat.user2 == request.user:      
            messageReceiver = chat.user1
            temp = chat.unread1
            chat.unread1 = temp +1
            chat.save(update_fields=['unread1'])
        else:      
            messageReceiver = chat.user2 
            temp = chat.unread2
            chat.unread2 = temp +1
            chat.save(update_fields=['unread2'])     
        newMessage = Message(        
            chat = chat,        
            sender = request.user,                                                     
            receiver = messageReceiver,        
            body = request.POST.get('message'),                
        )     
        newMessage.save()       
        return redirect('chat', pk = pk)
    

def showMessages(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        form = messageForm()
        chat = Chat.objects.get(pk = pk)   
        message_list = Message.objects.filter(chat__pk__contains = pk)
        if chat.user1 == request.user:
            temp = 0
            chat.unread1 = temp
            chat.save(update_fields=['unread1'])
        if chat.user2 == request.user:
            temp = 0
            chat.unread2 = temp
            chat.save(update_fields=['unread2'])
        context = {      
            'chat': chat,      
            'form': form,      
            'message_list': message_list    
        }   
        return render(request, 'chat.html', context)




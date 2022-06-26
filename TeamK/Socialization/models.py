from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     Year = models.IntegerField()
#     Major = models.CharField(max_length=100)

# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()

class Chat(models.Model):  
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    unread1 = models.IntegerField(default=0)
    unread2 = models.IntegerField(default=0)

class Message(models.Model):  
    chat = models.ForeignKey('Chat', related_name='+', on_delete=models.CASCADE, blank=True, null=True)  
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')  
    body = models.CharField(max_length=1000)  
    date = models.DateTimeField(auto_now_add=True)  
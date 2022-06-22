from django.db import models

# Create your models here.

class User(models.Model):
    Username = models.CharField(max_length=10, unique=True)
    Password = models.CharField(max_length=50)
    Name = models.CharField(max_length=20)
    Year = models.IntegerField(MinValueValidator = 1900)
    Major = models.CharField(max_length=10, choices=open('Majors.txt').readlines())

class ChatMessage(models.Model):
    ChatRoomName = models.CharField(max_length=100)
    receiver = models.CharField(max_length=10)
    sender = models.CharField(max_length=10, unique=True)
    message = models.CharField(max_length=1000)
    date = models.DateField()



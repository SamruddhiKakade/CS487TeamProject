from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Information(models.Model):
    # Username = models.CharField(max_length=10, unique=True)
    # Password = models.CharField(max_length=50)
    # Name = models.CharField(max_length=20)
    # Year = models.IntegerField()
    # Major = models.CharField(max_length=100)

    user = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    Name = models.CharField(max_length=20)
    Year = models.IntegerField()
    Major = models.CharField(max_length=100)


    # Name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    # Year = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    # Major = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')


class ChatMessage(models.Model):
    ChatRoomName = models.CharField(max_length=100)
    receiver = models.CharField(max_length=10000)   #String containing list of users allowed to look at message
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    message = models.CharField(max_length=1000)
    date = models.DateField()


# class ChatRoom(models.Model):
#     User1 =
#     User2 =
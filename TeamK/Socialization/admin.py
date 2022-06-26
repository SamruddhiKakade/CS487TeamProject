# from django.contrib import admin
# from models import Information,ChatMessage
#
# # Register your models here.
# admin.site.register(Information)
# admin.site.register(ChatMessage)



from django.contrib import admin
from .models import Chat,Message

# Register your models here.
admin.site.register(Chat)
admin.site.register(Message)


"""TeamK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.contrib import admin
import django.contrib.auth 
from Socialization import views as socviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    # path('profile/', socviews.profile, name='profile'),
    path('home/', socviews.home, name='home'),
    path('search/', socviews.search, name='search'),
    path('searchResult/', socviews.searchResult, name='searchResult'),
    path('', socviews.register, name='register'),
    path('register', socviews.register, name='register'),
    path('Messages', socviews.showChats, name='Messages'),
    path('Messages/newchat', socviews.newChat, name='newchat'),
    path('Messages/<int:pk>/', socviews.showMessages, name='chat'),
    path('Messages/<int:pk>/NewMessage/', socviews.newMessage, name='NewMessage'),
    path('openSearch',socviews.openSearch,name='openSearch'),
]
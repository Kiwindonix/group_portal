from django.shortcuts import render
from auth_system.models import CustomUser

# Create your views here.

def create_users(request):
    
    CustomUser.objects.create_user(username="john", email="josd@example.com", password="1")
    CustomUser.objects.create_user(username="nick", email="jo@example.com", password="2")
    CustomUser.objects.create_user(username="vlad", email="jsn@example.com", password="3")
    CustomUser.objects.create_user(username="ivan", email="jn@example.com", password="4")
    CustomUser.objects.create_user(username="vitya", email="j@example.com", password="5")

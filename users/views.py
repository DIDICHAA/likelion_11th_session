from django.shortcuts import render, redirect
from django.contrib import auth

def mypage(request):
    return render(request, 'users/mypage.html')

# Create your views here.

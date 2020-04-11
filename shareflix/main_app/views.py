from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(req):
    return render(req, 'home.html')

def info(req):
    return render(req, 'info.html')

def user(req):
    return render(req, 'profile.html')
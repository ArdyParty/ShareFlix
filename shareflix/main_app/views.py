from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from .models import Movie


# Create your views here.

def home(req):
    return render(req, 'home.html')

def info(req):
    return render(req, 'info.html')

# def profile(req, user_id):
#     user = User.objects.get(id=user_id)
#     return render(req, 'profile.html')

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'how_heard', 'where', 'description']

class MovieList(ListView):
    model = Movie
    fields = ['title']
    
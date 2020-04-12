from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from .models import Movie, User
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

@login_required
def home(req):
    return render(req, 'home.html')

def info(req):
    return render(req, 'info.html')

def signup(req):
    error_message = ''
    if req.method == 'POST':
        # This is how to create a 'user' form object that includes the data from the browser
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save() # Add the user to the database
            login(req, user) # Log a user in via code
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(req, 'registration/signup.html', context)

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'how_heard', 'where', 'description']

class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    fields = ['title']

class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie

class MovieUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = '__all__'
    template_url = 'movie_form.html'
    success_url = '/mylist/'
    
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

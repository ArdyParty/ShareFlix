from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Movie, Profile, Following
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 


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

class WatchableCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'how_heard', 'where', 'description']

    # def form_valid(self, form):
    #     form.instance.user = self.request.user  # Assign the currently logged in user(self.request.user) to the current movie instance
    #     return super().form_valid(form)# Validates and saves the instance to the database
    def form_valid(self, form):
        form.instance.profile_id = self.request.user.profile.id  # Assign the currently logged in user(self.request.user) to the current movie instance
        return super().form_valid(form) # Validates and saves the instance to the database
    
class WatchableUpdate(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'how_heard', 'where', 'description', 'genre', 'watched']

class WatchableDelete(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = '/mylist/'

class WatchableList(LoginRequiredMixin, ListView):
    model = Movie
    fields = ['title']

class WatchableDetail(LoginRequiredMixin, DetailView):
    model = Movie
    
class ProfileDetail(LoginRequiredMixin, DetailView):
    model = Profile

class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    success_url = '/user/1/'

def follow(req, user_id):
    f = Following()
    f.profile_id = req.user.profile.id
    f.follow_id = req.user.profile.id
    f.save()
    
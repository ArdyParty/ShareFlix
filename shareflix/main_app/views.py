from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Movie, Profile, Following
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # NOTE: Currently not using UserChangeForm
from .forms import UserForm, ProfileForm



# Create your views here.

@login_required
def home(req):
    return render(req, 'home.html')

def info(req):
    return render(req, 'info.html')

def signup(req):
    #error_message = ''
    if req.method == 'POST':
        print('Foo')
        # This is how to create a 'user' form object that includes the data from the browser
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save() # Add the user to the database
            login(req, user) # Log a user in via code
            return redirect('home')
    #     else:
    #         error_message = 'Invalid sign up - try again'
    # # A bad POST or a GET request, so render signup.html with an empty form
    # form = UserCreationForm()
    # context = {'form': form, 'error_message': error_message}
    # return render(req, 'registration/signup.html', context) # redirect to login page
    print('bar')
    return redirect('login') # redirect to login page

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
    fields = '__all__'
    # fields = [ 'username', 'first_name', 'last_name','email']


def follow(req, profile_id):
    f = Following()
    f.profile_id = req.user.profile.id
    f.follow_id = profile_id
    f.save()
    return render(req, 'home.html')
    
class FollowingList(LoginRequiredMixin, ListView):
    model = Following

# def settings(req):
#     error_message = ''
#     #profile = user.profile
#     if req.method == 'POST':
#         user_form = UserForm(req.POST)
#         profile_form = ProfileForm(req.POST)
#         if user_form.is_valid():
#             # Get current profile and update with form stuff
#             # request.userprofile. = settings_form.save()
#             #user = user_form.save()
#             #profile = profile_form.save()
#             return redirect('home')
#         else:
#             error_message = 'Invalid Settings'
#     # A bad POST or a GET request, so render signup.html with an empty form
#     #user_form = UserForm()
#     profile_form = ProfileForm()
#     # context = {'form': form, 'error_message': error_message}
#     # return render(request, 'home/', context) # FIX route
#     return render(req, 'main_app/profile_detail.html', {
#         #'user_form': user_form, 
#         'profile_form': profile_form,
#         'error_message': error_message
#         })

def settings(request):
    user = request.user # Current user
    profile = user.profile # Current user's profile
    if (request.method == 'POST'):
        user_form = UserForm(request.POST or None, instance=user) # Once you change the instance arg from a new object to an existing one
        profile_form = ProfileForm(request.POST or None, instance=profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_update = user_form.save(commit=False)
            profile_update = profile_form.save(commit=False)
            user_update.id = user.id
            profile_update.id = profile.id
            user_form.save()
            profile_form.save()
            return redirect('profile_detail', user.id)
    user_form = UserForm(instance=user) # Start off with users data
    profile_form = ProfileForm(instance=profile)
    context = {'user_form': user_form,'profile_form': profile_form,}
    return render(request, 'main_app/settings.html', context)
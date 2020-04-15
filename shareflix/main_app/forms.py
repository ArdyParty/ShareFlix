from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        labels = {
            'email': 'Email',
        }
        help_texts = {
            'username': '', # Remove the default help_text
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['fave_movie']
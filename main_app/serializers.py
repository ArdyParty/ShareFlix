from rest_framework import serializers
from .models import Movie, Profile

class MovieSerializer(serializers.ModelSerializer):
  class Meta:
    model = Movie
    fields = ('id', 'profile', 'title', 'where', 'how_heard')


class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = ( 'user', 'fave_movie', 'quote', 'profile_photo_url')
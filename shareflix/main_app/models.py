from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now

# date: Defaults to the current date and time
# title: The title of the movie
# how_heard: How or from whom did you hear about the movie
# where: Where or how can you view the movie
# description: A small blurb about what the movie is about 
# genre: The genre of the movie
# watched: Defaults to false when you add the movie to your profile

class Movie(models.Model):
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100)
    how_heard = models.TextField(max_length=1000, default='', blank=True)
    where = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(max_length=1000, default='', blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 1:M, a user can recommend many movies

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date'] # Sort from most most recent to old
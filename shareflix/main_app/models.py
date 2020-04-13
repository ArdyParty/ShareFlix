from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

# date: Defaults to the current date and time
# title: The title of the movie
# how_heard: How or from whom did you hear about the movie
# where: Where or how can you view the movie
# description: A small blurb about what the movie is about 
# genre: The genre of the movie
# watched: Defaults to false when you add the movie to your profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    fave_movie = models.CharField(max_length=100, default='', blank=True)
    # TODO: Add avater and cover fields

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'Profile {self.id} belongs to user_id {self.user}'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Following(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    follow = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="follow")

class Movie(models.Model):
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100)
    how_heard = models.TextField(max_length=1000, default='', blank=True)
    where = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(max_length=1000, default='', blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)
    watched = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # 1:M, a profile can have many movies

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date'] # Sort from most most recent to old
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    fave_movie = models.CharField(max_length=100, default='', blank=True, verbose_name='Favourite movie')
    quote = models.TextField(max_length=1000, default='', blank=True, verbose_name='Favourite movie/show quote')
    profile_photo_url = models.CharField(max_length=200, default='', blank=True, verbose_name='Profile photo URL')

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.id})

    def __str__(self):
        return f'{self.user}({self.user.id})\'s profile({self.id})'

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Following(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='profile')
    follow = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='follow')

    def __str__(self):
        return f'{self.profile.user} follows {self.follow.user}'

    class Meta:
        constraints = [models.UniqueConstraint(fields=['profile', 'follow'], name='unique_following')] # Prevents multiple entires for following someone

class Movie(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE) # 1:M, a profile can have many movies
    date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100)
    how_heard = models.TextField(max_length=1000, default='', blank=True)
    where = models.CharField(max_length=100, default='', blank=True)
    description = models.TextField(max_length=1000, default='', blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)
    watched = models.BooleanField(default=False)
    recommend = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('watchable_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['-date'] # Sort from most most recent to old